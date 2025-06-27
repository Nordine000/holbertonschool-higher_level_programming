-- cree une table force et ne plante pas si elle existe avec comme champ id et name de type varchar qui ne doit pas etre null
CREATE TABLE IF NOT EXISTS force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);
