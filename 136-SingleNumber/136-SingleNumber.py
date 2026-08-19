# Last updated: 8/18/2026, 5:57:11 PM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        # xor
4        res = 0
5
6        for num in nums:
7            res ^= num
8        
9        return res