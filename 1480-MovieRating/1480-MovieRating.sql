-- Last updated: 8/16/2026, 9:48:18 PM
# Write your MySQL query statement below
(
select name as results
from Users u left join MovieRating mr using(user_id)
group by u.user_id
order by count(distinct movie_id) desc, name asc limit 1
)
union all -- union all to avoid poeple name is the same as movie title
(
select title as results
from Movies m left join MovieRating mr using(movie_id)
where substring(created_at, 1, 7) = '2020-02'
group by m.movie_id
order by avg(rating) desc, title asc limit 1
)

