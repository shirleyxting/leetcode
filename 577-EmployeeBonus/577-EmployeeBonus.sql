-- Last updated: 8/16/2026, 9:49:58 PM
# Write your MySQL query statement below
select name, bonus
from Employee left join Bonus using(empId)
where bonus < 1000 or bonus is null