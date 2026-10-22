select *
from cinema
where 
    (case 
        when id % 2 = 1 then id 
    end) and description != "boring"
order by rating DESC;