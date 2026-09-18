# Last updated: 9/17/2026, 8:19:12 PM
1class Solution:
2    def shipWithinDays(self, weights: list[int], days: int) -> int:
3        # binary search on answer
4        # 1. given 'days'
5        # 2. find min of max_capacity, which is in [max(weights), sum(weights)]
6        # 3. feasible(X): given each day capacity <= X, get the min days needed -> 'T'
7        # 4. return T <= days
8        #  then for each max_capacity, you will see feasible() returns: F F T T T
9        #  we want the leftmost T
10
11        def feasible(X: int) -> bool:
12            curr, min_days = 0, 1
13            for w in weights:
14                curr += w
15                if curr > X:
16                    min_days += 1
17                    curr = w
18            return min_days <= days
19        
20        left, right = max(weights), sum(weights)
21        res = 0
22        while left <= right:
23            mid = (left + right) // 2
24            if feasible(mid):
25                res = mid
26                right = mid - 1
27            else:
28                left = mid + 1
29        
30        return res
31
32