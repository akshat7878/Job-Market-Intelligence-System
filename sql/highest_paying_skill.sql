SELECT
    s.skill_name,
    ROUND(AVG(sa.med_salary),2) AS avg_salary
FROM salaries sa
JOIN postings p
ON sa.job_id = p.job_id
JOIN job_skills js
ON p.job_id = js.job_id
JOIN skills s
ON js.skill_abr = s.skill_abr
WHERE sa.med_salary IS NOT NULL
GROUP BY s.skill_name
HAVING COUNT(*) > 50
ORDER BY avg_salary DESC
LIMIT 10;