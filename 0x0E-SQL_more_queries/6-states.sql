-- creating a databse and a table inside it with values 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- creating a table init with values
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT NOT NULL UNIQUE AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id));
