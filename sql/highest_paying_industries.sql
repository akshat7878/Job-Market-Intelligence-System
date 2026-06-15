SELECT
    i.industry_name,
    ROUND(AVG(p.normalized_salary), 2) AS avg_salary
FROM postings p
JOIN job_industries ji
ON p.job_id = ji.job_id
JOIN industries i
ON ji.industry_id = i.industry_id
WHERE p.normalized_salary IS NOT NULL
GROUP BY i.industry_name
HAVING COUNT(*) > 20
ORDER BY avg_salary DESC
LIMIT 10;