SELECT
    s.skill_name,
    COUNT(*) AS demand,
    ROUND(AVG(sa.med_salary),2) AS avg_salary
FROM job_skills js
JOIN skills s
ON js.skill_abr = s.skill_abr
JOIN salaries sa
ON js.job_id = sa.job_id
WHERE sa.med_salary IS NOT NULL
GROUP BY s.skill_name
HAVING COUNT(*) > 100
ORDER BY demand DESC;