-- Last updated: 8/16/2026, 9:48:39 PM
# Write your MySQL query statement below
select distinct viewer_id as id
from Views
where viewer_id = author_id 
order by id