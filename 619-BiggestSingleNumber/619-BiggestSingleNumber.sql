-- Last updated: 8/16/2026, 9:49:43 PM
# Write your MySQL query statement below
select max(num) as num
from (
    select num
    from MyNumbers
    group by num
    having count(*) = 1
) t
