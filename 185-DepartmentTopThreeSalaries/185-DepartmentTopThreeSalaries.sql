-- Last updated: 8/16/2026, 9:51:40 PM
# Write your MySQL query statement below
-- with temp as (
--     select *,
--     dense_rank() over(partition by departmentId order by salary desc) as salary_rank
--     from Employee
-- )
-- select d.name as Department, e.name as Employee, e.salary
-- from temp e join Department d 
--     on e.departmentId = d.id
-- where salary_rank <= 3 

-- without window function
select d.name as Department,
    e.name as Employee,
    e.salary
from Employee e join Department d 
    on e.departmentId = d.id
where e.id in (
    select e1.id
    from Employee e1 left join Employee e2
        on e1.departmentId = e2.departmentId and e1.salary < e2.salary 
    group by e1.id
    having count(distinct e2.salary) < 3
)
