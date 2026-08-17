-- Last updated: 8/16/2026, 9:48:34 PM
# Write your MySQL query statement below
select substring(trans_date, 1, 7) as month, country,
    count(*) as trans_count,
    sum(case when state = 'approved' then 1 else 0 end) as approved_count,
    sum(amount) as trans_total_amount,
    sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from Transactions
group by substring(trans_date, 1, 7), country