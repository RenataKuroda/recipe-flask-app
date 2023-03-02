from flask import Flask, render_template, request, redirect, session
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash, check_password_hash

from models.recipe import get_all_recipes, get_recipe_by_id

app = Flask(__name__)

@app.route('/')
def index():
    recipes = get_all_recipes()

    return render_template('index.html', recipes=recipes)

if __name__ == "__main__":
    app.run(debug = True)

@app.route('/recipe/<id>')
def recipe_detail(id):
    recipe = get_recipe_by_id(id)
    return render_template('recipe_details.html', recipe=recipe)


@app.route('/new-recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'GET':
        return render_template('new_recipe.html')

    title = request.form.get('title')
    description = request.form.get('description')
    image_url = request.form.get('image_url')

    # Parse ingredients
    ingredient_names = request.form.getlist('ingredient_name')
    ingredient_amounts = request.form.getlist('ingredient_amount')
    ingredient_units = request.form.getlist('ingredient_unit')

    ingredients = []
    for name, amount, unit in zip(ingredient_names, ingredient_amounts, ingredient_units):
        if name and amount and unit:
            ingredients.append(f'{amount} {unit} {name}')

    ingredients = '\n'.join(ingredients)

    # Parse instructions
    step_instructions = request.form.getlist('step_instruction')
    step_numbers = request.form.getlist('step_number')

    instructions = []
    for instruction, number in zip(step_instructions, step_numbers):
        if instruction:
            instructions.append(f'{number}. {instruction}')

    instructions = '\n'.join(instructions)

    # Save recipe to database
    insert_recipe(title, description, ingredients, instructions, image_url)

    return redirect('/')