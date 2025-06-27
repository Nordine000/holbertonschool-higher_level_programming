-- cree une table unique_id avec un id avec une valeur defaut et une contrainte unique(chaque valeur est dif)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
    );
