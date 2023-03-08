INSERT INTO recipes (title, description, ingredients, instructions, image_url, created_at, course, user_id)
VALUES ('Classic Margherita Pizza', 'A classic pizza made with tomato sauce, mozzarella cheese, and fresh basil', 
        '{"Pizza dough","Tomato sauce","Mozzarella cheese","Fresh basil"}',

        '{"Preheat the oven to 4Q50°F.","Roll out the pizza dough to the desired thickness and shape.","Spread tomato sauce over the dough leaving a small border around the edges.","Add the mozzarella cheese on top of the sauce.","Bake the pizza in the oven for 10-12 minutes or until the crust is golden brown.","Remove the pizza from the oven and top with fresh basil leaves."}', 
        'https://images.unsplash.com/photo-1600028068383-ea11a7a101f3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80', DATE_TRUNC('day', NOW()),'main', 2
        );

INSERT INTO recipes (title, description, ingredients, instructions, image_url, created_at, course, user_id)
VALUES ('Spinach and Feta Stuffed Chicken', 
        'This recipe is an easy and flavorful way to enjoy chicken. The spinach and feta cheese stuffing adds a pop of flavor and nutrition to your meal.',
        '{"4 boneless, skinless chicken breasts","2 cups fresh spinach","1/2 cup crumbled feta cheese","1 tablespoon olive oil","1 tablespoon garlic powder","salt and pepper to taste"}', 
        '{"Preheat oven to 375°F.","In a skillet, heat olive oil over medium heat.","Add spinach and cook until wilted.","Remove from heat and stir in feta cheese.","Slice a pocket into each chicken breast.","Stuff each chicken breast with spinach and feta mixture.","Sprinkle garlic powder, salt, and pepper over the chicken.","Place chicken breasts in a baking dish and bake for 25-30 minutes, or until chicken is cooked through."}',
        'https://media.istockphoto.com/id/118313946/photo/chicken-breasts-stuffed-with-spinach-and-feta.jpg?s=612x612&w=is&k=20&c=RoMZTAJvrgDQCGERiVEKmSjxoObr7CZYYoe9ZQaZz5I=', DATE_TRUNC('day', NOW()), 'main', 1
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