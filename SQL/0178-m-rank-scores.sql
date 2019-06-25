SELECT
  Score,
  (SELECT count(DISTINCT Score) FROM Scores WHERE Score >= s.Score) AS Rank
FROM Scores s
ORDER BY Score desc