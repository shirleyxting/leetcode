# Last updated: 9/19/2026, 10:17:23 PM
1class Solution:
2    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
3        # binary search on the answer
4        # 1. fixed threshold
5        # 2. return the divisor (in range [1, max(nums)])
6        # 3. if divisor is X, can we have sum(num/ X) <= threshold (divide is math.ceil()), get the sum of the divisons: T
7        # 4. return T <= threshold
8
9        # F F T T T T, find the leftmost T
10
11        def feasible(X: int) -> bool:
12            div_sum = 0
13            for num in nums:
14                div_sum += math.ceil(num / X)
15            
16            return div_sum <= threshold
17        
18        left, right = 1, max(nums)
19        res = 0
20        while left <= right:
21            mid = (left + right) // 2
22            if feasible(mid):
23                res = mid
24                right = mid - 1
25            else:
26                left = mid + 1
27        
28        return res