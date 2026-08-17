-- Last updated: 8/16/2026, 9:48:23 PM
# Write your MySQL query statement below
select c1.visited_on, 
    SUM(c2.amount) amount, 
    ROUND(SUM(c2.amount)/7, 2) average_amount
from (
    select DISTINCT visited_on
    from Customer
    where date_add(visited_on, interval -6 day) >= (
        select MIN(visited_on) from Customer
    )
) c1 
join Customer c2
    on DATEDIFF(c1.visited_on, c2.visited_on) between 0 and 6
GROUP BY c1.visited_on