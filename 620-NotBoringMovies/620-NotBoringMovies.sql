-- Last updated: 8/16/2026, 9:49:38 PM
# Write your MySQL query statement below
select *
from Cinema
where id % 2 = 1 and description <> 'boring'
order by rating desc