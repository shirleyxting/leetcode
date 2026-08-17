# Last updated: 8/16/2026, 9:52:43 PM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # for every h, take it as the actual height for rectangle
        # for each curr_h, extend left, right to find the left-neareast small, right-nearest small
        #   left_boundry, right_boundry, and all h in (left_boundry, right_boundry) satisfing "h >= curr_h"
        #   area = (right_b - left_b - 1) * curr_h

        # heights = [2,1,5,6,2,3]
        # for curr_h=2:
        #     h=6, left_b=5, right_b=2, ->width=4-2-1=1, area=6*1=6
        #      =5,        1,         2,        =4-1-1=2, area=5*2=10
        # monotonic stack

        stack = [] # save index, montonic increasing stack
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            # sentinol node: height[n] = 0, to clear stack
            curr_height = heights[i] if i < n else 0

            while stack and curr_height < heights[stack[-1]]:
                height = heights[stack.pop()]
                left_boundry = stack[-1] if stack else -1
                width = i - left_boundry - 1
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        return max_area
