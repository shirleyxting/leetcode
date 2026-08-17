-- Last updated: 8/16/2026, 9:51:35 PM
# Write your MySQL query statement below
-- DELETE from Person where id not in (
--     select min(id) as id
--     from Person as p
--     group by email
-- )
-- you will be noted " You can't specify target table 'Person' for update in FROM clause ",
-- The solution is using a middle table with select clause:
DELETE from Person where id not in (
    select id from (
        select min(id) as id
        from Person
        group by email
    ) t
)