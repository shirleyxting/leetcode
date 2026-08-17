-- Last updated: 8/16/2026, 9:47:44 PM
# Write your MySQL query statement below
-- select category, count(distinct account_id) as accounts_count
-- from (
--     select (
--         case when income < 20000 then 'Low Salary'
--             when (income >= 20000 and income <= 50000) then 'Average Salary'
--             else 'High Salary'
--         end
--         ) as category, 
--         account_id
--     from Accounts
-- ) t
-- group by category
-- this will miss the 'average salary' (no record satisfy the income range)
-- use UNION to ensure all 3 categories show up
select 'Low Salary' as category,
    sum(case when income < 20000 then 1 else 0 end) as accounts_count
from Accounts
UNION
select 'Average Salary' as category,
    sum(case when (income >= 20000 and income <= 50000) then 1 else 0 end) as accounts_count
from Accounts
UNION
select 'High Salary' as category,
    sum(case when income > 50000 then 1 else 0 end) as accounts_count
from Accounts