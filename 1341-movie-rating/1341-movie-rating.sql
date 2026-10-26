(select name as results from users
join movierating using (user_id)
group by user_id
order by count(rating) DESC, name
limit 1)

union all

(select title as results from movies 
join movierating using (movie_id)
where year(created_at) = '2020' and month(created_at) = '02' 
group by movie_id
order by avg(rating) DESC, title
limit 1)