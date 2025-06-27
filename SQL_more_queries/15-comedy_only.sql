--script qui liste toutes les séries de genre Comédie dans la base de données hbtn_0d_tvshows
SELECT t.title
FROM tv_shows AS t, tv_show_genres AS m, tv_genres AS g
WHERE t.id = m.show_id
  AND g.id = m.genre_id
  AND g.name = 'Comedy'
ORDER BY t.title ASC;
