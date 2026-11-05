select 
    max(salary) as SecondHighestSalary 
from (
    select 
    salary,
    dense_rank() over (order by salary DESC) as rnk
    from employee
) as temp
where rnk = 2;