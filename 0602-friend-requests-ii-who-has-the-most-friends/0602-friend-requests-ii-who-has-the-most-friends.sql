select 
    requester_id as id,
    count(*) as num
from (select requester_id  from RequestAccepted 
    UNION ALL
    select accepter_id from RequestAccepted 
    ) as frd_count
group by requester_id
order by num DESC
limit 1;