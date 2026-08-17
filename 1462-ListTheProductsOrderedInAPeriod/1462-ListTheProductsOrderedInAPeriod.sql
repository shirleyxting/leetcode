-- Last updated: 8/16/2026, 9:48:20 PM
# Write your MySQL query statement below
-- with t as (
--     select product_id, sum(unit) as unit
--     from Orders
--     where substring(order_date, 1, 7) = '2020-02'
--     group by product_id
--     having sum(unit) >= 100
-- )
-- select product_name, unit
-- from products p join t using(product_id)

select product_name, sum(unit) as unit
from products p join Orders o using(product_id)
where substring(order_date, 1, 7) = '2020-02'
group by product_id
having sum(unit) >= 100

