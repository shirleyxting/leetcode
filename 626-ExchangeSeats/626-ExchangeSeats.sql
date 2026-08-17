-- Last updated: 8/16/2026, 9:49:35 PM
# Write your MySQL query statement below
-- select s1.id, 
--     (case when id%2=1 
--             then ifnull(lead(student, 1) over (order by id), student)
--         when id%2=0 then lag(student, 1) over (order by id)
--     end) as student
-- from Seat s1 
-- order by s1.id

-- or modify id, keep student
-- even id -> odd id
-- odd id -> even id, if odd id is not the last id
select (
    case when id%2=0 then id-1
    when (id%2=1 and id < (
        select max(id) from Seat
    )) then id+1
    else id
    end
) as id, student
from Seat
order by id