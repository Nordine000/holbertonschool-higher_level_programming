-- repertorie toutes les villes de Californie qui peuvent etre troyver dans la base de donnee
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
