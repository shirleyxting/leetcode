# Last updated: 8/16/2026, 9:53:26 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                res = mid
                break

            if nums[left] <= nums[mid]:
                # [left, mid] is sorted
                if nums[left] <= target <= nums[mid]:
                    # move left
                    right = mid - 1 
                else: # even though the remaining is not sorted, target must sits in the remaining right part [mid, right]
                    # move right
                    left = mid + 1
            else:
                # [mid, right] is sorted
                if nums[mid] <= target <= nums[right]:
                    # move right
                    left = mid + 1
                else: # target sits in the remaining un-sorted left part [left, mid]
                    # move left
                    right = mid - 1
        
        return res



