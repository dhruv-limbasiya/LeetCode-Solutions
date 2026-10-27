with first_login as (
    select player_id, min(event_date) as first_login
    from activity
    group by player_id
)

select 
    round(count(*)/(select count(distinct player_id) from activity) , 2) as fraction
from first_login f
join activity a
on a.player_id = f.player_id and datediff(a.event_date, f.first_login) = 1;