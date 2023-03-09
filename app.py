from flask import Flask, render_template, request, redirect, session
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash, check_password_hash
from cloudinary import CloudinaryImage
import cloudinary.uploader
import os

from models.recipe import get_all_recipes, get_recipe, insert_recipe, delete_recipe, update_recipe, get_user_recipes, get_all_recipes_by_search, get_all_recipes_by_course, get_all_dairy_free_recipes
from models.users import get_user_by_email, insert_user

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

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
    
    if not user:
        message = "Email not registered. Please try again with a different email."
        return render_template('login_form.html', message=message)
    
    password_matches = check_password_hash(user['password_hash'], password)

    if not password_matches:
        message = "Incorrect password. Please try again."
        return render_template('login_form.html', message=message)
    
    session['user_id'] = user['id']
    session['user_name'] = user['name']
    session['user_email'] = user['email']
    return redirect('/')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    user = get_user_by_email(email)
    
    if user:
        message = "This email is already registered. Please try again with a different email."
        return render_template('signup.html', message=message)
    
    if password != confirm_password:
        message = "Passwords do not match. Please try again."
        return render_template('signup.html', message=message)
    
    if len(password) < 8:
        message = "Password must be at least 8 characters long and contain letters and numbers."
        return render_template('signup.html', message=message)
    
    password_hash = generate_password_hash(password)

    insert_user(name, email, password_hash)
    return redirect('/login')

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
        message = "To be able to post your own recipes, please login."
        return render_template('login_form.html', message=message)
        
    if request.method == 'GET':
        return render_template('new_recipe.html')

    title = request.form.get('title')
    description = request.form.get('description')

    if 'image' in request.files:
        # Upload the image to Cloudinary
        image = request.files.get('image')
        uploaded_image = cloudinary.uploader.upload(image)
        image_url = uploaded_image['url']
    else:
        # Set a default image URL or use a placeholder image
        image_url = 'https://images.unsplash.com/photo-1487260211189-670c54da558d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80'

    user_id = session['user_id']
    course = request.form.get('course')

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
    
    dairy_free = request.form.get('dairy_free')
    gluten_free = request.form.get('gluten_free')
    low_carb = request.form.get('low_carb')
    no_added_sugar = request.form.get('no_added_sugar')
    nut_free = request.form.get('nut_free')
    vegan = request.form.get('vegan')
    vegetarian = request.form.get('vegetarian')

    insert_recipe(title, description, ingredients, instructions, image_url, course, user_id, dairy_free, gluten_free, low_carb, no_added_sugar, nut_free, vegan, vegetarian)

    return redirect('/')    

@app.route('/my-recipes')
def my_recipes():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = session['user_id']
    user_recipes = get_user_recipes(session['user_id'])

    return render_template('my_recipes.html', user_recipes=user_recipes)

@app.route('/course/<course>')
def course_result(course):
    recipes = get_all_recipes_by_course(course)

    return render_template('search.html', recipes=recipes)

@app.route('/dairy-free')
def dairy_free():
    recipes = get_all_dairy_free_recipes()

    return render_template('search.html', recipes=recipes)

@app.route('/search')
def search_result():
    query = request.args.get('query')
    recipes = get_all_recipes_by_search(query)

    return render_template('search.html', recipes=recipes)

@app.route('/delete-recipe/<id>', methods=['POST'])
def delete_recipe_item(id):
    delete_recipe(id)
    return redirect('/')

@app.get('/edit-recipe/<id>')
def update_recipe_form(id):
    recipe = get_recipe(id)
    print(recipe)
    return render_template("edit_recipe.html", id=id, title=recipe['title'], description=recipe['description'], ingredients=recipe['ingredients'], instructions=recipe['instructions'], image_url=recipe['image_url'], course=recipe['course'], gluten_free=recipe['gluten_free'], dairy_free=recipe['dairy_free'], low_carb=recipe['low_carb'], nut_free=recipe['nut_free'], no_added_sugar=recipe['no_added_sugar'], vegan=recipe['vegan'], vegetarian=recipe['vegetarian'])

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

    course = request.form.get('course')

    dairy_free = request.form.get('dairy_free')
    gluten_free = request.form.get('gluten_free')
    low_carb = request.form.get('low_carb')
    no_added_sugar = request.form.get('no_added_sugar')
    nut_free = request.form.get('nut_free')
    vegan = request.form.get('vegan')
    vegetarian = request.form.get('vegetarian')

    update_recipe(id, title, description, ingredients, instructions, course, dairy_free, gluten_free, low_carb, no_added_sugar, nut_free, vegan, vegetarian)

    return redirect('/my-recipes')