WITH salary_cte AS (
    SELECT DISTINCT salary
    FROM Employee
)
SELECT MAX(salary) AS SecondHighestSalary
FROM salary_cte
WHERE salary < (
    SELECT MAX(salary)
    FROM salary_cte
);
