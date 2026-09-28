# Last updated: 9/27/2026, 4:07:17 PM
1class Solution:
2    def sortColors(self, nums: list[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        counter = Counter(nums)
7        
8        for i in range(counter[0]):
9            nums[i] = 0
10        for i in range(counter[0], counter[0] + counter[1]):
11            nums[i] = 1
12        for i in range(counter[0] + counter[1], len(nums)):
13            nums[i] = 2
14        
15        