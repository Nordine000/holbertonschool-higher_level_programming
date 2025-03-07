-- répertorie toutes les villes contene dans la base de dnees hbtn_0d_u
SELECT cities.id AS id, cities.name AS name, states.name AS name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
