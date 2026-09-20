# Last updated: 9/20/2026, 1:38:01 PM
1class Solution:
2#  binary search on answer
3# 1. fixed k
4# 2. return max #of candies, #candies in range [0, max(candies)] 
5# (canides=[1,100], k=1), just think whats the max number that ONE child can get
6# 3. feasible(X): given #of candies, X, can u split it into k people
7# the number of splits: T = sum(num//T, for num in candies)
8# 4.return T >= k
9# T T T F F, get the rightmost T
10    def maximumCandies(self, candies: list[int], k: int) -> int:
11        def feasible(X: int) -> bool:
12            count = 0
13            for c in candies:
14                count += c // X
15            return count >= k
16        
17        # c // X, so left starts from 1
18        left, right = 1, max(candies)
19        res = 0 # res init as 0, if returns F F F F, we can just return res=0
20
21        while left <= right:
22            mid = (left + right) // 2
23            if feasible(mid):
24                # move right
25                res = mid
26                left = mid + 1
27            else:
28                right = mid - 1
29        
30        return res