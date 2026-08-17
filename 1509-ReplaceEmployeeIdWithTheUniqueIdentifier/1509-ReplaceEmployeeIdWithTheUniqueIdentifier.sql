-- Last updated: 8/16/2026, 9:48:15 PM
# Write your MySQL query statement below
select unique_id, name
from Employees left join EmployeeUNI using(id)
