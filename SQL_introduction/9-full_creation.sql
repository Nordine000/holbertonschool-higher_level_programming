-- script qui crée une table second_table dans la base de données hbtn_0c_0 de ton serveur MySQL et y insère plusieurs lignes
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table (id, name, score)
VALUES (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);
