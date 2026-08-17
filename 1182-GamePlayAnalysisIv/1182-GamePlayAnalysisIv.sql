-- Last updated: 8/16/2026, 9:48:45 PM
# Write your MySQL query statement below
-- select round(
--     count(distinct a1.player_id) / (
--         select count(distinct player_id)
--         from Activity
--     )
--     , 2) as fraction
-- from (
--     select player_id, min(event_date) as first_date
--     from Activity
--     group by player_id
-- ) a1 
-- join Activity a2
--     on a1.player_id = a2.player_id
--     and datediff(a2.event_date, a1.first_date) = 1

-- or since (player_id, event_date) is primary key
-- (player_id, event_date - 1 day [should = min date]) can also be used to filter records
select round(
    count(distinct player_id) / (
        select count(distinct player_id)
        from Activity 
    ), 2) as fraction
from Activity
where (player_id, date_add(event_date, interval -1 day)) in (
    select player_id, min(event_date)
    from Activity
    group by player_id
)
