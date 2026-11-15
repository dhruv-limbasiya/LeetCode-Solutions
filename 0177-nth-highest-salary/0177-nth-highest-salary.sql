CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
RETURN 
    (
        select distinct salary
        from (
            select
                salary,
                dense_rank() over (order by salary DESC) as rnk 
            from employee
        ) as ranked
        where rnk = N
    );
end