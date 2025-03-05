-- répertorie tous les enregistrements de la table second_tabl
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
