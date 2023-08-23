import psycopg2
from psycopg2.extras import RealDictCursor

import db

def get_all_recipes():
    all_recipes = db.select_all("SELECT * FROM recipes ORDER BY created_at DESC")
    return all_recipes

def get_recipe(id):
    recipe = db.select_one("SELECT * from recipes WHERE id = %s", [id])
    return recipe

def insert_recipe(title, description, ingredients, instructions, image_url, course, user_id, dairy_free=False, gluten_free=False, low_carb=False, no_added_sugar=False, nut_free=False, vegan=False, vegetarian=False,):
    db.insert(
        "INSERT INTO recipes (title, description, ingredients, instructions, image_url, course, user_id, dairy_free, gluten_free, low_carb, no_added_sugar, nut_free, vegan, vegetarian) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        [title, description, ingredients, instructions, image_url, course, user_id, dairy_free or None, gluten_free or None, low_carb or None, no_added_sugar or None, nut_free or None, vegan or None, vegetarian or None]
    )

def delete_recipe(id):
    db.write('DELETE FROM recipes WHERE id = %s', 
    [id]
    )

def update_recipe(id, title, description, ingredients, instructions, course, dairy_free=False, gluten_free=False, low_carb=False, no_added_sugar=False, nut_free=False, vegan=False, vegetarian=False):
    db.write('UPDATE recipes SET title = %s, description = %s, ingredients = %s, instructions = %s, course = %s, dairy_free = %s, gluten_free = %s, low_carb = %s, no_added_sugar = %s, nut_free = %s, vegan = %s, vegetarian = %s WHERE id = %s', 
    [title, description, ingredients, instructions, course, dairy_free or None, gluten_free or None, low_carb or None, no_added_sugar or None, nut_free or None, vegan or None, vegetarian or None, id]
    )

def get_user_recipes(user_id):
    my_recipes = db.select_all_recipes_by_param('SELECT * FROM recipes WHERE user_id = %s ORDER BY created_at DESC', [user_id])
    return my_recipes

def get_all_recipes_by_search(query):
    all_recipes = db.select_all_recipes_by_param("SELECT * FROM recipes WHERE title ILIKE %s OR %s = ANY(ingredients) OR EXISTS(SELECT 1 FROM unnest(ingredients) AS i WHERE i ILIKE %s) ORDER BY created_at DESC", [f"%{query}%", query, f"%{query}%"])
    return all_recipes

def get_all_recipes_by_course(course):
    all_recipes = db.select_all_recipes_by_param("SELECT * from recipes WHERE course = %s ORDER BY created_at DESC", [course])
    return all_recipes

def get_all_dairy_free_recipes():
    dairy_free_recipes = db.select_all("SELECT * from recipes WHERE dairy_free")
    return dairy_free_recipes

def get_all_gluten_free_recipes():
    gluten_free_recipes = db.select_all("SELECT * from recipes WHERE gluten_free")
    return gluten_free_recipes

def get_all_low_carb_recipes():
    low_carb_recipes = db.select_all("SELECT * from recipes WHERE low_carb")
    return low_carb_recipes

def get_all_no_added_sugar_recipes():
    no_added_sugar_recipes = db.select_all("SELECT * from recipes WHERE no_added_sugar")
    return no_added_sugar_recipes

def get_all_nut_free_recipes():
    nut_free_recipes = db.select_all("SELECT * from recipes WHERE nut_free")
    return nut_free_recipes

def get_all_vegan_recipes():
    vegan_recipes = db.select_all("SELECT * from recipes WHERE vegan")
    return vegan_recipes

def get_all_vegetarian_recipes():
    vegetarian_recipes = db.select_all("SELECT * from recipes WHERE vegetarian")
    return vegetarian_recipes

def get_user_recipes_by_search(user_id, query):
    my_search_recipes = db.select_all_recipes_by_param('SELECT * FROM recipes WHERE user_id = %s AND (title ILIKE %s OR %s = ANY(ingredients) OR EXISTS(SELECT 1 FROM unnest(ingredients) AS i WHERE i ILIKE %s))', [user_id, f"%{query}%", query, f"%{query}%"])
    return my_search_recipes

def insert_favorite(user_id, recipe_id):
    db.insert(
        "INSERT INTO favorites (user_id, recipe_id) VALUES (%s, %s)",
        [user_id, recipe_id]
    )

