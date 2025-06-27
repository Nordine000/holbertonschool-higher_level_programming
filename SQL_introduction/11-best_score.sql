-- Un script qui liste les enregistrements ayant un score supérieur ou égal à 10 dans la table second_table
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
