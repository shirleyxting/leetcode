-- Last updated: 8/16/2026, 9:49:48 PM
# Write your MySQL query statement below
select class
from Courses
group by class
having count(distinct student) >= 5