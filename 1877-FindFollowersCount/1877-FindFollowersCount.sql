-- Last updated: 8/16/2026, 9:47:56 PM
# Write your MySQL query statement below
select user_id, count(distinct follower_id) as followers_count
from Followers
group by user_id
order by user_id