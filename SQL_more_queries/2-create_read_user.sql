-- cree une base de donn√es, si elle existe elle doit pas echouer
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- crre un utilisateur avec sont mot de passe, si il existe il ne doit pas echouer
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- accored tt les privilege a l'user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
