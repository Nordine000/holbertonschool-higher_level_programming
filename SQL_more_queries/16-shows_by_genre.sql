-- repertorie toute les emissions et genre lier a cette emission dans la base de donnees
SELECT s.title, g.name
FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
LEFT JOIN tv_genres g ON sg.genre_id = g.id
ORDER BY s.title ASC, g.name ASC;
