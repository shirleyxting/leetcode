-- Last updated: 8/16/2026, 9:48:09 PM
# Write your MySQL query statement below
select *
from Users
where mail regexp '^[A-Za-z]+[A-Za-z0-9\_\.\-]*@leetcode[.]com$' 
-- ^ means the begining of string
-- [A-Za-z]+: + means at least one of the char exists
-- [A-Za-z0-9\_\.\-]*: * means 0 or more char exists
-- since '.' is a special character, it matches anything including '?'. To make it work, use two backslashes '@leetcode\\.com', which gives '@leetcode\.com' for regexp matching. Alternatively, you can put '.' inside [], where it has no special meaning so no escape needed, like so: '@leetcode[.]com'.
-- ($) represents the end of a line