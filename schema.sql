-- createdb recipeapp
-- psql recipeapp

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(155),
    ingredients TEXT[] NOT NULL,
    instructions TEXT[] NOT NULL,
    image_url TEXT,
    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
    course VARCHAR(255) NOT NULL,
    user_id INTEGER NOT NULL,
    CONSTRAINT fk_user_id
        FOREIGN KEY(user_id)
        REFERENCES users(id)
    dairy_free BOOLEAN NOT NULL DEFAULT false,
    gluten_free BOOLEAN NOT NULL DEFAULT false
    low_carb BOOLEAN NOT NULL DEFAULT false,
    no_added_sugar BOOLEAN NOT NULL DEFAULT false,
    nut_free BOOLEAN NOT NULL DEFAULT false,
    vegan BOOLEAN NOT NULL DEFAULT false,
    vegetarian BOOLEAN NOT NULL DEFAULT false
);

CREATE TABLE users(
    id SERIAL PRIMARY KEY, 
    email TEXT NOT NULL,
    name TEXT NOT NULL,
    password_hash TEXT
);


-- to create favorite's list for each user
CREATE TABLE favorites (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    recipe_id INTEGER NOT NULL,
    CONSTRAINT fk_user_id
        FOREIGN KEY(user_id)
        REFERENCES users(id),
    CONSTRAINT fk_recipe_id
        FOREIGN KEY(recipe_id)
        REFERENCES recipes(id)
);
-- to add a recipe to a user's favorites list
INSERT INTO favorites (user_id, recipe_id) VALUES (1, 2);

-- to retrieve users favorite
SELECT recipes.id, recipes.title, recipes.image_url
FROM favorites
JOIN recipes ON favorites.recipe_id = recipes.id
WHERE favorites.user_id = 1;

-- SELECT recipes.*
-- FROM favorites
-- JOIN users ON favorites.user_id = users.id
-- JOIN recipes ON favorites.recipe_id = recipes.id
-- WHERE users.id = <user_id>;
