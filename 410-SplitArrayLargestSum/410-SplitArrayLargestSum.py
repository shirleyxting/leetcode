# Last updated: 9/17/2026, 5:04:45 PM
1class Solution:
2    # ① 给定：k splits
3    # ② 答案：whats the min of largest subarrary sum X，范围 [max(nums), sum(nums)]
4    # ③ feasible(X)：每组和卡死 ≤ X，贪心算最少组数 T
5    # ④ 返回：T <= k     单调：X 越大 → T 越小 → F F T T T --> return the first T 
6    def splitArray(self, nums: list[int], k: int) -> int:
7        def feasible(X: int) -> bool:
8            # for each subarrary sum <= X, whats the min of splits (T)
9            # return T <= k (means under the limit of k splits, its feasible to have each subarrary_sum <= X )
10            curr, splits = 0, 1
11            for num in nums:
12                curr += num
13                if curr > X:
14                    splits += 1
15                    curr = num
16
17            return splits <= k
18        
19        left, right = max(nums), sum(nums)
20        res = 0
21        while left <= right:
22            mid = (left + right) // 2
23            if feasible(mid):
24                # move left to find leftmost
25                # F F T T T T
26                res = mid
27                right = mid - 1
28            else:
29                left = mid + 1
30        
31        return res
32