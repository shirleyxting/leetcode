-- Last updated: 8/16/2026, 9:48:36 PM
# Write your MySQL query statement below
-- step 1: fetch the first order for each customer_id
-- step 2: calculate immediate_percentage
select round( 100 * (
    sum(case when order_date  = customer_pref_delivery_date then 1 else 0 end)  
    / count(distinct customer_id)
    ), 2) as immediate_percentage
from Delivery
where (customer_id, order_date) in (
    select customer_id, min(order_date)
    from Delivery
    group by customer_id
)
