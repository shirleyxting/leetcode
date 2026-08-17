-- Last updated: 8/16/2026, 9:48:31 PM
# Write your MySQL query statement below
select person_name
from Queue
where turn = (
    select q1.turn
    from Queue q1 left join Queue q2
        on q1.turn >= q2.turn
    group by q1.turn
    having sum(q2.weight) <= 1000
    order by sum(q2.weight) desc limit 1
)
