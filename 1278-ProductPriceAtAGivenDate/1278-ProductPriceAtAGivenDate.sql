-- Last updated: 8/16/2026, 9:48:37 PM
# Write your MySQL query statement below

select product_id, new_price as price
from Products
where (product_id, change_date) in (
    select product_id, max(change_date)
    from Products p 
    where change_date <= '2019-08-16'
    group by product_id
)
union 
select product_id, 10 as price
from Products
group by product_id
having min(change_date) > '2019-08-16'

-- or just get the product that NOT have change_date <= '2019-08-16' 
-- select product_id, 10 as price
-- from Products
-- where product_id not in (
--     select distinct product_id
--     from Products
--     where change_date <= '2019-08-16'
-- )