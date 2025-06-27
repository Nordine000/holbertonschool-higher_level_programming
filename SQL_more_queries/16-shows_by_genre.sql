-- Un script qui liste toutes les séries ainsi que tous les genres associés à chaque série depuis la base de données hbtn_0d_tvshows
SELECT
    t.title,
    g.name
FROM
    tv_shows AS t
LEFT JOIN
    tv_show_genres AS m
ON
    t.id = m.show_id
LEFT JOIN
    tv_genres AS g
ON
    g.id = m.genre_id
ORDER BY
    title ASC,
    name ASC;
