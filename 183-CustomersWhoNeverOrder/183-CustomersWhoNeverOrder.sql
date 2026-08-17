-- Last updated: 8/16/2026, 9:51:43 PM
# Write your MySQL query statement below
-- select name as customers
-- from Customers c 
-- where id not in (
--     select distinct customerId 
--     from Orders o 
-- ) 

-- or using join
select c.name as customers
from Customers c left join Orders o 
    on c.id = o.customerId
where o.customerId is null