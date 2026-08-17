-- Last updated: 8/16/2026, 9:49:47 PM
# Write your MySQL query statement below
-- with temp as (
-- select requester_id as id,
--     count(*) as request_num,
--     0 as accept_num
-- from RequestAccepted  
-- group by requester_id
-- union all
-- select accepter_id as id,
--     0 as request_num,
--     count(*) as accept_num
-- from RequestAccepted  
-- group by accepter_id
-- )
-- select id,
-- sum(request_num) + sum(accept_num) as num
-- from temp
-- group by id
-- order by num desc limit 1

-- Union All is what you need! Don't Overcomplicate
with temp as (
    select requester_id as id
    from RequestAccepted
    union all
    select accepter_id as id
    from RequestAccepted
)
select id, count(*) num
from temp
group by id
order by num desc limit 1;