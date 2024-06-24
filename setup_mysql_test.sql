-- SQL file to set up the hbnb_test_db database and hbnb_test user
-- Creates the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creates the user if it does not exist and sets the password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grants all privileges on the hbnb_test_db database to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grants SELECT privilege on the performance_schema to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
