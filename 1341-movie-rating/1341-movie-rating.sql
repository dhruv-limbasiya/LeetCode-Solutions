(select name as results
from users join movierating using(user_id)
group by user_id
order by count(rating) DESC, name
limit 1)

UNION ALL

(select title as results
from movies join movierating using(movie_id)
where year(created_at) = "2020" and month(created_at) = "02"
group by movie_id
order by avg(rating) DESC, title
limit 1)


-- created_at between "2020-01-31" and "2020-03-01"