# Last updated: 8/16/2026, 9:52:11 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # order is un-realted info, so convert nums to hashset
        # each consecutive list is decided by start point, so iterating over start

        nums_set = set(nums)
        res = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                # if prev not found, then num must be the start
                # if prev presents, [prev ..] > [curr ..]
                # so we need to find the TRUE start of each consecutive list

                length = 1 # starts with num
                while num + length in nums_set:
                    length += 1
                
                res = max(res, length)
        
        return res
