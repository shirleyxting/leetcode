-- Last updated: 8/16/2026, 9:48:50 PM
# Write your MySQL query statement below
select product_id, year as first_year, quantity, price
from (
    select *, rank() over (partition by product_id order by year asc) as row_num
    from Sales s
) temp
where row_num = 1
/*
The question description is INCORRECT!

There are multiple sales in first year for each product. just return all of them separately.
There are some product_id are not in the Product Table, which should be removed from the query

like expected:
| product_id | first_year | quantity | price |
| ---------- | ---------- | -------- | ----- |
| 1          | 1802       | 67       | 1888  |
| 1          | 1802       | 30       | 3797  |

*/
-- row_number() will fail
/* 
       RANK() OVER(PARTITION BY StyleID ORDER BY ID)       AS [RANK],
       ROW_NUMBER() OVER(PARTITION BY StyleID ORDER BY ID) AS [ROW_NUMBER],
       DENSE_RANK() OVER(PARTITION BY StyleID ORDER BY ID) AS [DENSE_RANK]

StyleID     ID       RANK      ROW_NUMBER      DENSE_RANK
----------- -------- --------- --------------- ----------
1           1        1         1               1
1           1        1         2               1
1           1        1         3               1
1           2        4         4               2
*/