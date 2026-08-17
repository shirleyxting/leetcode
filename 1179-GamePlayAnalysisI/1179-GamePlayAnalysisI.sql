-- Last updated: 8/16/2026, 9:48:47 PM
# Write your MySQL query statement below
select player_id, min(event_date) as first_login
from Activity
group by player_id