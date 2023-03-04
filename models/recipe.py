import psycopg2
from psycopg2.extras import RealDictCursor

import db

def get_all_recipes():
    all_recipes = db.select_all("SELECT id, title, description, ingredients, instructions, image_url, created_at from recipes ORDER BY created_at DESC")
    return all_recipes

def get_recipe(id):
    recipe = db.select_one("SELECT id, title, description, ingredients, instructions, image_url, created_at from recipes WHERE id = %s", [id])
    return recipe

def insert_recipe(title, description, ingredients, instructions, image_url):
    db.insert(
        "INSERT INTO recipes (title, description, ingredients, instructions, image_url) VALUES (%s, %s, %s, %s, %s)",
        [title, description, ingredients, instructions, image_url]
    )

def delete_recipe(id):
    db.write('DELETE FROM recipes WHERE id = %s', 
    [id]
    )

def update_recipe(id, title, description, ingredients, instructions, image_url):
    db.write('UPDATE recipes SET title = %s, description = %s, ingredients = %s, instructions = %s, image_url = %s WHERE id = %s', 
    [title, description, ingredients, instructions, image_url, id]
    )