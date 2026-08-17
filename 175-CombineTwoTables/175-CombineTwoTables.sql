-- Last updated: 8/16/2026, 9:51:51 PM
# Write your MySQL query statement below
select firstName, lastName, city, state
from Person p left join Address a using(personId)
