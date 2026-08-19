# Last updated: 8/18/2026, 10:16:00 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        # res[i] = prefix * suffix
4        # get prefix first, for range(1,n)
5        # then multiply with num for range(n-2, -1, -1) -> [n-2:0]
6
7        n = len(nums)
8        res = [1] * n
9
10        # res[i] = nums[:i-1] multiply
11        for i in range(1, n):
12            res[i] = res[i-1] * nums[i-1]
13        
14        suffix = 1
15        for i in range(n-1, -1, -1):
16            res[i] *= suffix
17            suffix *= nums[i]
18        
19        return res