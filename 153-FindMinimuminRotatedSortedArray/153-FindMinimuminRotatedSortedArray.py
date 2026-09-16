# Last updated: 9/16/2026, 1:39:40 PM
1class Solution:
2    def findMin(self, nums: list[int]) -> int:
3        # [3,4,5,1,2] check if item <= last=2
4        #  F,F,F,T,T => the first T is what we want
5        # find first <= last val
6
7        n = len(nums)
8        last = nums[-1]
9        left, right = 0, n-1
10        res = -1
11
12        while left <= right:
13            mid = (left + right) // 2
14            if nums[mid] <= last:
15                # keep searching in the left
16                res = nums[mid]
17                right = mid - 1
18            else:
19                # move to right
20                left = mid + 1
21        
22        return res