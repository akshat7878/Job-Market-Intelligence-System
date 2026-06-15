SELECT
    s.skill_name,
    COUNT(*) AS demand
FROM job_skills js
JOIN skills s
ON js.skill_abr = s.skill_abr
GROUP BY s.skill_name
ORDER BY demand DESC
LIMIT 10;