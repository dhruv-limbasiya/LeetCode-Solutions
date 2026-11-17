select 
    score,
    dense_rank() over (order by score DESC) as 'rank'
from scores
order by score DESC;