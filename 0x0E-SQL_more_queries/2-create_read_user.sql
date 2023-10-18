-- creating a new user with select privileges only and a user password
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create a new user and password
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- give select privileges to the new user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
