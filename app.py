from flask import Flask, render_template, request, redirect, session
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from models.recipe import get_all_recipes, get_recipe_by_id, insert_recipe, delete_recipe

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

    ingredient_names = request.form.getlist('ingredient_name[]')

    ingredients = []
    for ingredient_name in ingredient_names:
        if ingredient_name:
            ingredients.append(ingredient_name)

    step_instructions = request.form.getlist('step_instruction[]')

    instructions = []
    for step_instruction in step_instructions:
        if step_instruction:
            instructions.append(step_instruction)

    insert_recipe(title, description, ingredients, instructions, image_url)

    return redirect('/')    

@app.route('/delete-recipe/<id>', methods=['POST'])
def delete_recipe_item(id):
    delete_recipe(id)
    return redirect('/')