# Last updated: 8/20/2026, 9:55:32 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left, right = 0, len(nums) - 1
4
5        while left <= right:
6            mid = (left + right) // 2
7            if nums[mid] == target:
8                return mid
9            elif nums[mid] < target:
10                left = mid + 1
11            else:
12                right = mid - 1
13            
14        return -1