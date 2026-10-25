select 
    d.name as department,
    e.name as employee,
    e.salary
from department d
join employee e
on e.departmentId = d.id
where e.salary in (
    select max(salary)
    from employee
    where departmentid = e.departmentid
)