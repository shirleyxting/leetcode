# Last updated: 8/16/2026, 9:53:21 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        # # water[i] = min(left_max, right_max) - height[i]
        # # brute force
        # n = len(height)
        # water = 0

        # for i in range(n):
        #     left_max = max(height[:i+1])
        #     right_max = max(height[i:])
        #     water += max(0, min(left_max, right_max) - height[i])
        
        # return water

        # dual-poniter
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
        
        return water
