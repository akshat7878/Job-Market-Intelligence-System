SELECT
    p.formatted_experience_level,
    ROUND(AVG(p.normalized_salary),2) AS avg_salary
FROM postings p
WHERE p.normalized_salary IS NOT NULL
GROUP BY p.formatted_experience_level
ORDER BY avg_salary DESC;