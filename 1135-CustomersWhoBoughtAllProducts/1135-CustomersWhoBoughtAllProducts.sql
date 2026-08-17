-- Last updated: 8/16/2026, 9:48:55 PM
# Write your MySQL query statement below
select customer_id
from Customer 
group by customer_id
having count(distinct product_key) = (
    select count(distinct product_key)
    from Product
)