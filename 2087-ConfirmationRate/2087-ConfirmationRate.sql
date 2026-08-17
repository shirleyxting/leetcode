-- Last updated: 8/16/2026, 9:47:37 PM
# Write your MySQL query statement below
select s.user_id, round(
    case when count(action) = 0 then 0
        else sum(case when action = 'confirmed' then 1 else 0 end) / count(action)
    end
    , 2) as confirmation_rate
from Signups s left join Confirmations c using(user_id)
group by user_id
