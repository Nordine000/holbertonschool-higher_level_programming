-- liste le nbre d'enregstremnt avec le meme score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
