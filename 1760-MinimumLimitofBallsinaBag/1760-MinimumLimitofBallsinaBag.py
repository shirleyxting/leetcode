# Last updated: 9/20/2026, 10:09:19 AM
1class Solution:
2    # binary search on answer
3    # 1. fixed maxOp
4    # 2. return max number of balls in a bag, in range [1, max(nums)]
5    # 3. feasible(X): given max number of balls in a bag, X. can u finish the division within maxOp?   we can get the min OP: T
6    # 4. return T <= maxOp
7    # 一袋 n 个球要拆到每袋 ≤ X，最少要拆成 ceil(n / X) 袋，每拆一次多一袋，所以 ceil(n/X) - 1 次
8    # T = Σ (ceil(n/X) - 1)，
9    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
10        def feasible(X: int) -> bool:
11            min_op = 0
12            for num in nums:
13                min_op += math.ceil(num / X) - 1
14            
15            return min_op <= maxOperations
16        
17        left, right = 1, max(nums)
18        res = 0
19        while left <= right:
20            mid = (left + right) // 2
21            if feasible(mid):
22                res = mid
23                right = mid - 1
24            else:
25                left = mid + 1
26        return res