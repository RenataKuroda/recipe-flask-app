import psycopg2
from psycopg2.extras import RealDictCursor

import db

def get_all_recipes():
    all_recipes = db.select_all("SELECT id, title, description, ingredients, instructions, image_url, created_at, course from recipes ORDER BY created_at DESC")
    return all_recipes

def get_recipe(id):
    recipe = db.select_one("SELECT id, title, description, ingredients, instructions, image_url, created_at, course from recipes WHERE id = %s", [id])
    return recipe

def insert_recipe(title, description, ingredients, instructions, image_url, course, user_id):
    db.insert(
        "INSERT INTO recipes (title, description, ingredients, instructions, image_url, course, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        [title, description, ingredients, instructions, image_url, course, user_id]
    )

def delete_recipe(id):
    db.write('DELETE FROM recipes WHERE id = %s', 
    [id]
    )

def update_recipe(id, title, description, ingredients, instructions, image_url, course):
    db.write('UPDATE recipes SET title = %s, description = %s, ingredients = %s, instructions = %s, image_url = %s, course = %s WHERE id = %s', 
    [title, description, ingredients, instructions, image_url, course, id]
    )

def get_user_recipes(user_id):
    my_recipes = db.select_all_recipes_by_user('SELECT * FROM recipes WHERE user_id = %s', [user_id])
    return my_recipes

def get_all_recipes_by_search(query):
    all_recipes = db.select_all_recipes_by_param("SELECT * from recipes WHERE title ILIKE %s", [f"%{query}%"])
    return all_recipes

def get_all_recipes_by_course(course):
    all_recipes = db.select_all_recipes_by_param("SELECT * from recipes WHERE course = %s", [course])
    return all_recipes