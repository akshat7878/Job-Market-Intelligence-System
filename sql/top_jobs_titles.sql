SELECT
    title,
    COUNT(*) AS jobs
FROM postings
GROUP BY title
ORDER BY jobs DESC
LIMIT 10;