select 
    a.machine_id,
    round(
        (select avg(a1.timestamp) from activity a1 where activity_type = "end" and a.machine_id = a1.machine_id) - 
        (select avg(a1.timestamp) from activity a1 where activity_type = "start" and a.machine_id = a1.machine_id),
    3) as processing_time
from activity a
group by a.machine_id;