SELECT
    work_type,
    ROUND(AVG(normalized_salary), 2) AS avg_salary,
    COUNT(*) AS jobs
FROM postings
WHERE normalized_salary IS NOT NULL
GROUP BY work_type
ORDER BY avg_salary DESC;