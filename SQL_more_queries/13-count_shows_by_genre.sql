-- liste tous les genres présents dans la base hbtn_0d_tvshows et affiche le nombre de séries associées à chaque genre
SELECT
    g.name AS genre,
    COUNT(m.show_id) AS number_of_shows
FROM
    tv_genres AS g
INNER JOIN
    tv_show_genres AS m
ON
    g.id = m.genre_id
GROUP BY
    g.name
ORDER BY
    number_of_shows DESC;
