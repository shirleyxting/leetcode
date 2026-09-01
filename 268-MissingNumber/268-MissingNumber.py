# Last updated: 8/31/2026, 10:44:44 PM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        # XOR: nums ^ range(n) -> even occurence = 0, odd occurence = 1 -> the missing one
4
5        n = len(nums)
6        res = n     # put n in res first, as nums index [0, n-1]
7
8        # we want to achieve: 0^1^2^...^(n-1)^n ^ nums[0]^nums[1]^...^nums[n-1]
9        for i, num in enumerate(nums):
10            res ^= i ^ num
11        
12        return res