-- Creer la base de donnees 'hbtn_0d_usa' et la tabl'states'
-- Requête pour créer une table d'états avec 2 contrain
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
