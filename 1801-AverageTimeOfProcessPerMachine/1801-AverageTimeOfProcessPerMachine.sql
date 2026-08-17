-- Last updated: 8/16/2026, 9:48:01 PM
# Write your MySQL query statement below
-- select machine_id, 
--     round(sum(
--         (CASE WHEN activity_type = 'start' then timestamp * (-1)
--             ELSE timestamp
--             END)
--     ) / count(distinct process_id), 3) as processing_time
-- from Activity
-- group by machine_id

-- self join
select a1.machine_id,
    round( sum(a2.timestamp - a1.timestamp) / count(distinct a1.process_id)
    , 3) as processing_time
from Activity a1 join Activity a2 on 
    a1.machine_id = a2.machine_id
    and a1.process_id = a2.process_id
    and a1.activity_type = 'start'
    and a2.activity_type = 'end'
group by machine_id