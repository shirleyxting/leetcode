-- Last updated: 8/16/2026, 9:49:44 PM
# Write your MySQL query statement below
select x, y, z,
    (case when 
        (x + y > z) and (x + z > y) and (y + z > x) 
        then 'Yes'
        else 'No'
    end) as triangle
from Triangle