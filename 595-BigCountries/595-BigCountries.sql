-- Last updated: 8/16/2026, 9:49:53 PM
# Write your MySQL query statement below
select name, population, area
from World
where area >= 3000000
    or population >= 25000000