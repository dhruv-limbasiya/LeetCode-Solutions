select
    id,
    count(*) as num
from (
    select requester_id as id from requestaccepted
    UNION ALL
    select accepter_id from requestaccepted
) as friend_count
group by id
order by num DESC
limit 1;