with first_login as(
    select player_id, min(event_date) as first_date
    from activity 
    group by player_id
)

select
    round(count(*) / (select count(distinct player_id) from activity), 2) as fraction
from first_login f
join activity a
on f.player_id = a.player_id and datediff(a.event_date,f.first_date) = 1;