-- Last updated: 8/16/2026, 9:48:04 PM
# Write your MySQL query statement below
-- with user_count as (
--     select count(distinct user_id) as user_cnt
--     from Users
-- )
-- select contest_id, round(
--     100 * (count(distinct r.user_id) / user_cnt)
--     , 2) as percentage
-- from Register r, user_count
-- group by contest_id
-- order by percentage desc, contest_id asc

-- or directly embed the user_count computation into 1 query
select contest_id, round(
    100 * ( count(distinct user_id ) / (select count(distinct user_id) from Users) )
    , 2) as percentage
from Register
group by contest_id
order by percentage desc, contest_id asc