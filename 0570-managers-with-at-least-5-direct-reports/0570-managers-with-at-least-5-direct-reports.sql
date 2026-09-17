select e.name
from employee e
inner join employee e2
on e.id = e2.managerid
group by e.id
having count(e2.managerid) >= 5;