-- createdb recipeapp
-- psql recipeapp

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    ingredients TEXT[] NOT NULL,
    instructions TEXT[] NOT NULL,
    image_url TEXT,
    created_at DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE users(
    id SERIAL PRIMARY KEY, 
    email TEXT NOT NULL,
    name TEXT NOT NULL,
    password_hash TEXT
);

