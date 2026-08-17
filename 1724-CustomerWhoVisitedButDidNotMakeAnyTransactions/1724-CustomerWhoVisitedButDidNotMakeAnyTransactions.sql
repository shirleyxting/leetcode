-- Last updated: 8/16/2026, 9:48:06 PM
# Write your MySQL query statement below
-- select customer_id, count(*) as count_no_trans
-- from Visits v 
-- where visit_id not in (
--     select visit_id
--     from Transactions
-- ) 
-- group by customer_id

-- or use left join, but null value
select customer_id, count(*) as count_no_trans
from Visits v left join Transactions t using(visit_id)
where t.visit_id is null
group by customer_id