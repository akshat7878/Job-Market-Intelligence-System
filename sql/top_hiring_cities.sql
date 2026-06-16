SELECT
    location,
    COUNT(*) AS jobs
FROM postings
WHERE location IS NOT NULL
GROUP BY location
ORDER BY jobs DESC
LIMIT 20;