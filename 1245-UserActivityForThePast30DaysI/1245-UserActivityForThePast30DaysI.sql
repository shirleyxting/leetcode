-- Last updated: 8/16/2026, 9:48:41 PM
# Write your MySQL query statement below
select activity_date as day, count(distinct user_id) as active_users
from Activity
-- where activity_date between date_add('2019-07-27', interval -29 day) and '2019-07-27'
-- or use datediff()
where datediff('2019-07-27', activity_date) between 0 and 29
    and activity_type is not null 
group by activity_date