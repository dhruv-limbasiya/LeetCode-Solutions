with first_max_salary as(
    select max(salary) as f_max_s
    from employee
)

select max(salary) as SecondHighestSalary 
from employee
where salary < (
    select * from first_max_salary
)