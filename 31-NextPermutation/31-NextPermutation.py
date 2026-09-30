# Last updated: 9/30/2026, 2:34:03 PM
1class Solution:
2    def nextPermutation(self, nums: list[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        # 1574 4 | 8532     # 1: find first decreasing point (pivot, 4)
7        # 1574 5 | 8432     # 2: in [8432], find first > pivot, switch
8        # 1574 5 | 2348     # 3: reverse 
9
10        n = len(nums)
11
12        i = n - 2
13        while i >= 0 and nums[i] >= nums[i+1]:
14            i -= 1
15        
16        # search [i+1: n), find first large than nums[i]
17        if i >= 0:
18            j = n - 1
19            while j > i and nums[j] <= nums[i]:
20                j -= 1
21            # switch i, j
22            nums[i], nums[j] = nums[j], nums[i]
23        
24        # reverse [i+1: n)
25        l, r = i+1, n-1
26        while l < r:
27            nums[l], nums[r] = nums[r], nums[l]
28            l += 1
29            r -= 1
30        
31
32
33
34
35
36
37