-- Last updated: 8/16/2026, 9:48:28 PM
# Write your MySQL query statement below
select query_name, 
    round(
        avg(rating / position)
        , 2) as quality,
    round(100 * (
        sum(case when rating < 3 then 1 else 0 end) / count(query_name)
        ), 2) as poor_query_percentage
from Queries q
where query_name is not null
group by query_name

