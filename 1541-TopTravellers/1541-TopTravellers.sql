-- Last updated: 8/16/2026, 9:48:15 PM
# Write your MySQL query statement below
select name, ifnull(sum(distance), 0) as travelled_distance
from Users u left join Rides r 
    on u.id = r.user_id
group by u.id
order by sum(distance) desc, name asc