-- Create table for users
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_nickname VARCHAR(255) NULL NULL PRIMARY KEY,
    hashed_email VARCHAR(255) NOT NULL,
    hashed_phone VARCHAR(255),
    hashed_password VARCHAR(255) NOT NULL,
    fidelity_score INTEGER
);

-- Create table for menus
CREATE TABLE plats (
    menu_id INTEGER PRIMARY KEY AUTOINCREMENT,
    menu_name VARCHAR(255),
    menu_description VARCHAR(255),
    price FLOAT,
    is_doubleable BOOL,
    doubled_price FLOAT,
    is_out_of_stock BOOL,
    is_online BOOL
);


-- Create table for supplements
CREATE TABLE supplements (
    supplement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplement_name VARCHAR(255),
    price FLOAT,
    is_out_of_stock BOOL,
    is_online BOOL
);
-- Create table for accompagnements
CREATE TABLE accompagnements (
    accompagnement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    accompagnement_name VARCHAR(255),
    price FLOAT,
    is_out_of_stock BOOL,
    is_online BOOL
);

-- Create table for desserts
CREATE TABLE desserts (
    dessert_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dessert_name VARCHAR(255),
    price FLOAT,
    is_out_of_stock BOOL,
    is_online BOOL
);