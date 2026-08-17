-- Last updated: 8/16/2026, 9:47:57 PM
# Write your MySQL query statement below
select tweet_id 
from Tweets
where length(content) > 15