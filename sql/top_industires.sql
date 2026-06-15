SELECT
    i.industry_name,
    COUNT(*) AS jobs_posted
FROM job_industries ji
JOIN industries i
ON ji.industry_id = i.industry_id
GROUP BY i.industry_name
ORDER BY jobs_posted DESC
LIMIT 10;