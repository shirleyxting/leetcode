-- Last updated: 8/16/2026, 9:48:07 PM
# Write your MySQL query statement below
select *
from Patients
where conditions like 'DIAB1%' or conditions like '% DIAB1%'