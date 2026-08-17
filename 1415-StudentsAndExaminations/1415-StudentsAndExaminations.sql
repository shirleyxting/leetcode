-- Last updated: 8/16/2026, 9:48:25 PM
# Write your MySQL query statement below
select temp.student_id, temp.student_name, temp.subject_name,
    count(e.student_id) as attended_exams
from (
    select * from Students s cross join Subjects
    ) temp left join Examinations e
    on temp.student_id = e.student_id
        and temp.subject_name = e.subject_name
group by temp.student_id, temp.subject_name
order by temp.student_id, temp.subject_name