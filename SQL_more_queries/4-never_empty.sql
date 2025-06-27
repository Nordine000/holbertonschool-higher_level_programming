-- creela table idnot_null avec 1 comme valeur par defaut pour l'id
CREATE TABLE IF NOT EXISTS id_not_null (
  id INT DEFAULT 1,
  name VARCHAR(256)
);
