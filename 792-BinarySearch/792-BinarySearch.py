# Last updated: 8/16/2026, 9:49:17 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l)//2 
            # '//' is the integer division, / will result to float type
            if nums[mid] == target: return mid
            elif nums[mid] < target: l = mid + 1
            else: r = mid - 1
        
        if nums[l] == target: return l
        
        return -1

