with turn_wise_weight as (
    select 
        person_name,
        turn,
        sum(weight) over (order by turn) as weight
    from queue
)

select 
    person_name
from turn_wise_weight 
where weight <= 1000
order by turn DESC
limit 1;