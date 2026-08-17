-- Last updated: 8/16/2026, 9:47:47 PM
# Write your MySQL query statement below
select employee_id, department_id
from Employee
group by employee_id
having count(distinct department_id) = 1
union
-- select employee_id, department_id
-- from Employee
-- where primary_flag = 'Y' 
--     and employee_id in (
--         select employee_id
--         from Employee
--         group by employee_id
--         having count(distinct department_id) > 1
--     )
-- for mulitple departments, only 1 record with primary_flag = 'Y' 
-- for single department, the  primary_flag = 'N' is always true
-- so condition 2 can be: 
select employee_id, department_id
from Employee
where primary_flag = 'Y' 