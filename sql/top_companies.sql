SELECT
    c.name,
    COUNT(*) AS jobs_posted
FROM postings p
JOIN companies c
ON p.company_id = c.company_id
GROUP BY c.name
ORDER BY jobs_posted DESC
LIMIT 10;