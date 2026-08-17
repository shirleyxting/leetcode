-- Last updated: 8/16/2026, 9:48:49 PM
# Write your MySQL query statement below
select project_id, 
    -- round(
    -- sum(ifnull(experience_years, 0)) / count(p.employee_id)
    -- , 2) as average_years 
    -- directly use AVG
    round(avg(experience_years), 2) as average_years 
from Project p left join Employee e using(employee_id)
where experience_years is not null -- a bug in testcase
group by project_id