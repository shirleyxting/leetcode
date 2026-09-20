# Last updated: 9/20/2026, 10:20:36 AM
1class Solution:
2    # binary search on the answer
3    # 1. fixed n: #of store,/splits
4    # 2. return the min of max num in all splits, in range of [1, max(quantities)]
5    # 3. feasible(X), given X, max num in all splits, can u distribute all products within n stores.
6    # return the min splits, T = sum(math.ceil(num/X) for num in nums)
7    # 4. return T <= n
8    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
9        def feasible(X: int) -> bool:
10            min_stores = 0
11            for q in quantities:
12                min_stores += math.ceil(q / X)
13            
14            return min_stores <= n
15        
16        left, right = 1, max(quantities)
17        res = 0
18        while left <= right:
19            mid = (left + right) // 2
20            if feasible(mid):
21                res = mid
22                right = mid - 1
23            else:
24                left = mid + 1
25        return res