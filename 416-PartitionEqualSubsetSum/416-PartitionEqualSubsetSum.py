# Last updated: 8/21/2026, 12:07:26 PM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        # total_sum % 2 == 1 -> False
4        #                  0 -> find one subset with sum = total_sum / 2
5        #  and each element can only be used once 
6        #  0/1 knapsack, with weights = 1, values = nums, capacity = total_sum / 2
7
8        total = sum(nums)
9        if total % 2 == 1:
10            return False
11        
12        target = total // 2
13
14        # dp[i][j]: for nums[:i], can it find subset sum = j
15        #  dp[i][j] = dp[i-1][j] (not pick num-i) OR dp[i-1][j-nums[i]] (pick num-i)
16        #   dp[i][j] only relies on dp[i-1], convert 2D to 1D, remove the row dimension
17        # dp[j], dp[j - num]
18        #   iterate j DESC in [target, num]
19        #   when process dp[j], dp[j-num] is not computed yet, still refers prev row
20        #   -> dp[i][j] = dp[i-1][j-num] (nums-i can only be used once)
21
22        dp = [False] * (target + 1)
23        
24        # dp[i][0]: for nums[i], empty subset can always reach sum = 0
25        dp[0] = True 
26
27        # dp[j]: its for rolling nums, 
28        #   if currently we procceed 2 nums, then dp[j] = dp[2][j], use 2 nums, can it get sum = j
29        #                            3                       3          3
30        #                            n                       n          whole nums[:]   
31        
32        for num in nums:
33            # iterate j DESC in [num, target]
34            for j in range(target, num - 1, -1):
35                dp[j] = dp[j] or dp[j-num]
36        
37        return dp[target]
38