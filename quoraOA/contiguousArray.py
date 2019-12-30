__author__ = ' Zhen Wang'

from typing import List


class Solution:

    def findMaxLen(self, nums: List[int]) -> int:
        arr = [-2 for i in range(2 * len(nums) + 1)]
        arr[len(nums)] = -1

        max_len, count = 0, 0
        for i in range(len(nums)):
            count = count + (-1 if nums[i] == 0 else 1)
            if arr[count + len(nums)] >= -1:
                max_len = max(max_len, i - arr[count + len(nums)])
            else:
                arr[count + len(nums)] = i

        return max_len




