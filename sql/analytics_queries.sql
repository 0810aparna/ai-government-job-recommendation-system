-- TOP IN-DEMAND SKILLS
SELECT extracted_skills
FROM jobs;

-- AVERAGE SALARY BY EXPERIENCE LEVEL
SELECT experience_level, AVG(salary_in_usd)
FROM salaries
GROUP BY experience_level;

-- TOP PAYING JOB ROLES
SELECT job_title, AVG(salary_in_usd) as avg_salary
FROM salaries
GROUP BY job_title
ORDER BY avg_salary DESC;

-- REMOTE JOB ANALYSIS
SELECT remote_ratio, AVG(salary_in_usd)
FROM salaries
GROUP BY remote_ratio;

-- GOVERNMENT SCHEMES BY CATEGORY
SELECT category, COUNT(*)
FROM government_schemes
GROUP BY category;