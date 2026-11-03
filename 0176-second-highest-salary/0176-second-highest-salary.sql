with max_salary as (select max(salary) as m_salary from employee)

select 
    max(salary) as SecondHighestSalary 
from employee
where salary < (select m_salary from max_salary);