create function getNthHighestSalary(N int) returns int
begin
return 
(
    select distinct salary
    from (
        select 
            salary,
            dense_rank() over (order by salary DESC) as rnk
        from employee
    ) as temp
    where rnk = N
);
end