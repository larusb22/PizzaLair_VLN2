INSERT INTO menu_menutype (name) VALUES ('Spicy');
INSERT INTO menu_menutype (name) VALUES ('Vegan');
INSERT INTO menu_menutype (name) VALUES ('Vegeterian');
INSERT INTO menu_menutype (name) VALUES ('Meat lovers');


INSERT INTO menu_menutoppingtype (name) VALUES ('Meat');
INSERT INTO menu_menutoppingtype (name) VALUES ('Greens');
INSERT INTO menu_menutoppingtype (name) VALUES ('Cheese');
INSERT INTO menu_menutoppingtype (name) VALUES ('Sauce');
INSERT INTO menu_menutoppingtype (name) VALUES ('Spice');


INSERT INTO menu_menutopping (name, type_id) VALUES ('Pepperoni', 1);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Ham', 1);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Bacon', 1);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Chicken', 1);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Pulled pork', 1);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Pineapple', 2);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Dates', 2);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Chili', 2);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Bell Pepper', 2);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Jalapeno', 2);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Mushrooms', 2);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Onion', 2);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Cheddar', 3);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Creamcheese', 3);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Vegancheese', 3);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Mozzarella', 3);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Black pepper', 4);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Oregano', 4);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Fresh basil', 4);
INSERT INTO menu_menutopping (name, type_id) VALUES ('BBQ', 5);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Chipotle', 5);
INSERT INTO menu_menutopping (name, type_id) VALUES ('Berneise', 5);



INSERT INTO menu_menuproduct (name, description, rating_id, type_id) VALUES ('Meat lovers madness', 'This pizza is what started Pizza Lair, its a fan favourite and will not leave you hanging.', 1, 4);
INSERT INTO menu_menuproduct (name, description, rating_id, type_id) VALUES ('The Spicy Southwest', 'This is an Alabama favourite, made with love', 2, 1);
INSERT INTO menu_menuproduct (name, description, rating_id, type_id) VALUES ('Vegan Savior', 'This pizza is for all my vegans out there', 3, 2);
INSERT INTO menu_menuproduct (name, description, rating_id, type_id, price, quantity)  VALUES ('Vegetarian Warrior', 'This pizza lives up to its name, trust me with this one', 4, 3, 1990, 1);


INSERT INTO menu_menurating (rating, total_ratings) VALUES (5, 1);
INSERT INTO menu_menurating (rating, total_ratings) VALUES (4, 1);
INSERT INTO menu_menurating (rating, total_ratings) VALUES (2, 4);

INSERT INTO menu_menuimage (image, menu_id) VALUES ('https://api.salescloud.is/sites/default/files/styles/large/public/products/dsc05660-3.jpg?itok=JUNeaQf1', 1);
INSERT INTO menu_menuimage (image, menu_id) VALUES ('https://api.salescloud.is/sites/default/files/styles/large/public/products/dsc05670-3.jpg?itok=VnsjeCuy', 2);
INSERT INTO menu_menuimage (image, menu_id) VALUES ('', 3);


INSERT INTO menu_menuproducttopping (menu_id, topping_id) VALUES (1, 23);
INSERT INTO menu_menuproducttopping (menu_id, topping_id) VALUES (1, 24);
INSERT INTO menu_menuproducttopping (menu_id, topping_id) VALUES (1, 25);
INSERT INTO menu_menuproducttopping (menu_id, topping_id) VALUES (1, 32);
INSERT INTO menu_menuproducttopping (menu_id, topping_id) VALUES (1, 36);
INSERT INTO menu_menuproducttopping (menu_id, topping_id) VALUES (1, 39);
INSERT INTO menu_menuproducttopping (menu_id, topping_id) VALUES (1, 42);


INSERT INTO offers_offers (name, description, product_id, offer_image, price) VALUES ('2 for 1', 'This is for families everywhere', )