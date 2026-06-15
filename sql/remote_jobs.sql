SELECT
    CASE
        WHEN remote_allowed = 1 THEN 'Remote'
        ELSE 'Not Remote'
    END AS job_type,
    COUNT(*) AS jobs
FROM postings
GROUP BY job_type;