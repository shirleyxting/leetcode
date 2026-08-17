-- Last updated: 8/16/2026, 9:47:36 PM
# Write your MySQL query statement below
select teacher_id, count(distinct subject_id) as cnt
from Teacher
group by teacher_id