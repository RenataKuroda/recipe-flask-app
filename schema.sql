CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL,
    image_url TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
