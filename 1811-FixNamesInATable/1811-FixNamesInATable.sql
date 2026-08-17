-- Last updated: 8/16/2026, 9:47:59 PM
# Write your MySQL query statement below
select user_id,
concat(
    upper(substring(name, 1, 1)),
    lower(substring(name, 2))
) as name
from Users
order by user_id