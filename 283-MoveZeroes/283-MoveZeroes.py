# Last updated: 8/16/2026, 9:50:42 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # non-zero counts
        # make nums[0~cnt] to nonZeros, and left as 0
        cnt = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cnt] = nums[i]
                cnt += 1
        
        for i in range(cnt, len(nums)):
            nums[i] = 0
        
        return


        