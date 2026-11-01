with turn_wise_weight as (
    select 
        person_name,
        turn,
        sum(weight) over (order by turn) as total_weight
        from queue
)

select 
    person_name
from turn_wise_weight 
where total_weight <= 1000
order by turn DESC 
limit 1;