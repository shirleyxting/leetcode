-- Last updated: 8/16/2026, 9:47:35 PM
# Write your MySQL query statement below
-- select e1.employee_id
-- from Employees e1 left join Employees e2
--     on e1.manager_id = e2.employee_id
-- where e1.salary < 30000
--     and e1.manager_id is not null
--     and e2.employee_id is null
-- order by e1.employee_id asc

-- or use subquery
select employee_id
from Employees
where salary < 30000
    and manager_id is not null
    and manager_id not in (
        select distinct employee_Id
        from Employees
    )
order by employee_id asc