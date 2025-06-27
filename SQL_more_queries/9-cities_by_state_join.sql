-- répertorie toutes les villes contenues dans la base de données hbtn_0d_usa
SELECT
    cities.id,
    cities.name,
    states.name
FROM cities
JOIN states
ON states.id = cities.state_id
ORDER BY cities.id ASC;
