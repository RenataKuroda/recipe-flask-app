from flask import Flask, render_template, request, redirect, session
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash, check_password_hash

from models.recipe import get_all_recipes, get_recipe, insert_recipe, delete_recipe, update_recipe, get_user_recipes
from models.users import get_user_by_email, insert_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'naoseiqualpalavrasecretaescolher';

@app.route('/')
def index():
    recipes = get_all_recipes()

    return render_template('index.html', recipes=recipes)

if __name__ == "__main__":
    app.run(debug = True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login_form.html')

    email = request.form.get('email')
    password = request.form.get('password')
    user = get_user_by_email(email)
    
    password_matches = check_password_hash(user['password_hash'], password)

    if password_matches:
        session['user_id'] = user['id']
        session['user_name'] = user['name']
        session['user_email'] = user['email']
        return redirect('/')
        
    else:
        return redirect('/login_form')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    password_hash = generate_password_hash(password)

    insert_user(name, email, password_hash)
    return redirect ('/login')

@app.post('/logout')
def logout_user():
    session.pop('user_id')
    session.pop('user_name')
    session.pop('user_email')
    return redirect('/')

@app.route('/recipe/<id>')
def recipe_detail(id):
    recipe = get_recipe(id)
    return render_template('recipe_details.html', recipe=recipe)

@app.route('/new-recipe', methods=['GET', 'POST'])
def add_recipe():
    if 'user_id' not in session:
        return redirect('/login')
        
    if request.method == 'GET':
        return render_template('new_recipe.html')

    title = request.form.get('title')
    description = request.form.get('description')
    image_url = request.form.get('image_url')
    user_id = session['user_id']

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

    insert_recipe(title, description, ingredients, instructions, image_url, user_id)

    return redirect('/')    

@app.route('/my-recipes')
def my_recipes():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = session['user_id']
    user_recipes = get_user_recipes(session['user_id'])
    for recipe in user_recipes:
        print(recipe)
    return render_template('my_recipes.html', user_recipes=user_recipes)


@app.route('/delete-recipe/<id>', methods=['POST'])
def delete_recipe_item(id):
    delete_recipe(id)
    return redirect('/')

@app.get('/edit-recipe/<id>')
def update_recipe_form(id):
    recipe = get_recipe(id)
    print(recipe)
    return render_template("edit_recipe.html", id=id, title=recipe['title'], description=recipe['description'], ingredients=recipe['ingredients'], instructions=recipe['instructions'], image_url=recipe['image_url'])

@app.route('/updated-recipe/<int:id>', methods=['POST'])
def edit_recipe_form(id):
    
    title = request.form.get('title')
    description = request.form.get('description')
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
    
    image_url = request.form.get('image_url')

    update_recipe(id, title, description, ingredients, instructions, image_url)

    return redirect('/')