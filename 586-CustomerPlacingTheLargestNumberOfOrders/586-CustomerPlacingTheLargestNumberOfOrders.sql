-- Last updated: 8/16/2026, 9:49:54 PM
# Write your MySQL query statement below

select customer_number
from Orders
group by customer_number
order by count(*) desc
limit 1;
