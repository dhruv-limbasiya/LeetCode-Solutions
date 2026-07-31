(select u.name as results from users u
join movierating m 
on u.user_id = m.user_id 
group by u.name, u.user_id
order by count(*) DESC, u.name ASC
limit 1)

UNION ALL
(
select m.title as results
from movies m
join movierating mr 
on m.movie_id = mr.movie_id
where created_at between '2020-02-01' and '2020-02-29'
group by m.movie_id, m.title
order by avg(rating) DESC, m.title ASC
LIMIT 1);