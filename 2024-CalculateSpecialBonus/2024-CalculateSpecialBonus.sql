-- Last updated: 8/16/2026, 9:47:46 PM
# Write your MySQL query statement below
select employee_id, 
    (case 
        when (employee_id % 2 = 0 or substring(name, 1, 1) = 'M') then 0
        else salary
    end) as bonus
from Employees 
order by employee_id