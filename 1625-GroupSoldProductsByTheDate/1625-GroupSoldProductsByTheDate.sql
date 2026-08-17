-- Last updated: 8/16/2026, 9:48:12 PM
# Write your MySQL query statement below
select sell_date, count(distinct product) as num_sold,
    group_concat(distinct product order by product ASC separator ',') as products
from Activities
group by sell_date
order by sell_date

-- GROUP_CONCAT