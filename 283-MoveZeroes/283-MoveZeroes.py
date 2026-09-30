# Last updated: 9/29/2026, 7:29:56 PM
1class Solution:
2    def moveZeroes(self, nums: list[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        # partition2 format
7        # keepLeft(): nums[i] != 0
8        # [0, left): keepLeft == True
9        # [left, i): keepLeft == False
10        # [i, n): unprocessed
11
12        left = 0
13        for i in range(len(nums)):
14            if nums[i] != 0:    # switch with left
15                nums[left], nums[i] = nums[i], nums[left]
16                left += 1
17        
18
19
20        