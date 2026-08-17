-- Last updated: 8/16/2026, 9:48:52 PM
# Write your MySQL query statement below
select product_name, year, price
from Sales left join Product using (product_id)