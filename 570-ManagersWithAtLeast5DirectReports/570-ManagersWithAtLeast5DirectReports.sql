-- Last updated: 8/16/2026, 9:50:05 PM
# Write your MySQL query statement below
select name
from Employee 
where id in (
    select e1.id
    from Employee e1 inner join Employee e2 
        on e1.id = e2.managerId
    group by e1.id
    having count(distinct e2.id) >= 5
)

-- group by id instead of name, cause you may have same people names for differnt person