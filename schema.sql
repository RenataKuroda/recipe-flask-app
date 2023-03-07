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
);

CREATE TABLE users(
    id SERIAL PRIMARY KEY, 
    email TEXT NOT NULL,
    name TEXT NOT NULL,
    password_hash TEXT
);

CREATE TABLE dietary_categories (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE
);

INSERT INTO dietary_categories (name) VALUES
('dairy-free'),
('gluten-free'),
('low-carb'),
('no added sugar'),
('nut-free'),
('paleo'),
('vegan'),
('vegetarian');

CREATE TABLE recipe_dietary_category (
  recipe_id INTEGER REFERENCES recipes(id),
  dietary_category_id INTEGER REFERENCES dietary_categories(id),
  PRIMARY KEY(recipe_id, dietary_category_id)
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
-- SELECT recipes.*
-- FROM favorites
-- JOIN users ON favorites.user_id = users.id
-- JOIN recipes ON favorites.recipe_id = recipes.id
-- WHERE users.id = <user_id>;
