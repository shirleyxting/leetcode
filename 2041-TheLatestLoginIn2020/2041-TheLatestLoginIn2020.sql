-- Last updated: 8/16/2026, 9:47:45 PM
# Write your MySQL query statement below
select user_id, max(time_stamp) as last_stamp
from Logins
where year(time_stamp) = 2020
group by user_id