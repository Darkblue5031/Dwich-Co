-- Sample data insertion for menus
INSERT INTO plats (menu_name, menu_description, price, is_doubleable, doubled_price, is_out_of_stock, is_online) VALUES
('Le DWICH', 'Bavette - Oignons Caramélisés - Tomates Confites - Provolone - Sauce Ranch - Moutarde', 9.00, TRUE, 12.00, FALSE, TRUE),
('Le SUPREME', 'Poulet - Bacon Fumé - Omelette - Cheddar - Oignons Rouges - Iceberg - Sauce Ranch', 9.00, FALSE, 9.00, FALSE, TRUE),
('Le PORZO', 'Araignée de Porc Marinée - Chorizo - Poivrons Marinés - Cheddar - Sauce Ranch', 8.50, FALSE, 8.50, TRUE, TRUE),
('Le CHICHE', 'Pois Chiche - Poivrons Marinés - Cheddar - Sauce Ranch', 8.50, FALSE, 8.50, TRUE, FALSE);

-- Sample data insertion for supplements
INSERT INTO supplements (supplement_name, price, is_out_of_stock, is_online) VALUES
('Sauce', 0.50, FALSE, TRUE),
('LEGUMES', 1.00, TRUE, TRUE),
('FROMAGE', 1.00, TRUE, FALSE),
('VIANDE', 3.00, FALSE, TRUE);

-- Sample data insertion for accompagnements
INSERT INTO accompagnements (accompagnement_name, price, is_out_of_stock, is_online) VALUES
('FRITES', 3.50, FALSE, TRUE),
('FRITES CAJUN', 3.50, FALSE, TRUE);

-- Sample data insertion for desserts
INSERT INTO desserts (dessert_name, price, is_out_of_stock, is_online) VALUES
('BANANA BREAD', 3.00, FALSE, FALSE),
