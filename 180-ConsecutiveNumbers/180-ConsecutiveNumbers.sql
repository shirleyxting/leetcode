-- Last updated: 8/16/2026, 9:51:46 PM
# Write your MySQL query statement below
-- select distinct l1.num as ConsecutiveNums 
-- from Logs l1, logs l2, logs l3
-- where l1.id + 1 = l2.id
--     and l2.id + 1 = l3.id
--     and l1.num = l2.num
--     and l2.num = l3.num

-- or use window_func lead()
select distinct num as ConsecutiveNums 
from (
    select num,
        lead(num, 1) over (order by id asc) as num_add1,
        lead(num, 2) over (order by id asc) as num_add2
    from Logs
) t
where num = num_add1 and num = num_add2


