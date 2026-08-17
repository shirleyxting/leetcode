-- Last updated: 8/16/2026, 9:49:45 PM
# Write your MySQL query statement below
select name
from SalesPerson
where sales_id not in (
    select distinct sales_id
    from Orders o left join Company c using(com_id)
    where c.name = 'RED'
)