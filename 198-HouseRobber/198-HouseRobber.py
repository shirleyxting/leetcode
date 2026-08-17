# Last updated: 8/16/2026, 9:51:29 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i]: max profit for nums[:i+1] (until nums[i])
        # for nums[i]: rob (dp[i-2]+nums[i]) or not rob (dp[i-1])
        # dp[i] = max( dp[i-2]+nums[i], dp[i-1] )
        # only previous two status required -> rolling variable instead of mainatining whole dp[] arr

        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        # init dp[-1], dp[0]
        prev2, prev1 = 0, nums[0]

        # iterate from house-1
        for i in range(1, len(nums)):
            curr = max(prev2 + nums[i], prev1)
            prev2, prev1 = prev1, curr
        
        return prev1