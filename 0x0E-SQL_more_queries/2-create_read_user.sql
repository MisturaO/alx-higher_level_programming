-- script that creates the database hbtn_0d_2 and the user user_0d_2.

-- creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates the user user_0d_2 with password 'user_0d_2_pwd'
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- Grant the user SELECT privilege
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
