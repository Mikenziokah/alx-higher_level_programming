-- creating a databse and a table inside it with values 
-- creating the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- open the database to create a table
USE hbtn_0d_usa;
--- creating a table init with values
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);