-- Last updated: 8/16/2026, 9:49:55 PM
# Write your MySQL query statement below
-- select round(sum(tiv_2016), 2) as tiv_2016
-- from Insurance
-- where pid in (
--     select pid
--     from Insurance 
--     group by lat, lon
--     having count(pid) = 1
-- )
-- and tiv_2015 in (
--     select tiv_2015
--     from Insurance
--     group by tiv_2015
--     having count(*) > 1
-- )

-- method 2 - window function
select round(sum(tiv_2016), 2) as tiv_2016
from (
    select *,
        count(*) over (partition by lat, lon) as cnt1,
        count(*) over (partition by tiv_2015) as cnt2
    from Insurance
) temp
where cnt1 = 1 and cnt2 > 1