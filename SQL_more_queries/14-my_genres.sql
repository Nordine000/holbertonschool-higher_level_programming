-- iste tous les genres associés à la série Dexter dans la base de données hbtn_0d_tvshows.
SELECT
    name
FROM
    tv_genres AS g
INNER JOIN
    tv_show_genres AS m
ON
    g.id = m.genre_id
INNER JOIN
    tv_shows t
ON
    m.show_id = t.id
WHERE
    t.title = 'Dexter'
ORDER BY
    name ASC;
