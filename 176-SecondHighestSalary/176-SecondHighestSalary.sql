-- Last updated: 8/16/2026, 9:51:49 PM
# Write your MySQL query statement below
select max(salary) as SecondHighestSalary 
from (
    select salary, dense_rank() over(order by salary desc) ranks
    from Employee
) temp
where ranks = 2

-- use MAX() to convert empty records to NULL values
