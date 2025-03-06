-- cree un utilisateur avec sont mpt de passe
CREATE USER IF NOT EXISTS 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd';
-- on lui donne tout les acces/privileges
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1';
