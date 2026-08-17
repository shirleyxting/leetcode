# Last updated: 8/16/2026, 9:51:53 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # # 2,2,1,1,1,2,2 -> 2
        # target_count = 0
        # if len(nums) % 2 == 0: 
        #     target_count = len(nums) // 2
        # else:
        #     target_count = len(nums) // 2 + 1
        
        # map = {}
        # for num in nums:
        #     map[num] = map.get(num, 0) + 1
        #     if map[num] > target_count:
        #         return num
        # return 

        # # sort, then return the item at "len/2" index
        # # if num occurs more than [n/2] times, it will always sit in the middle position [n/2] of the sorted nums
        # nums = sorted(nums)
        # return nums[len(nums) // 2]

        # method-3: linear time and O(1) space -- Moore's Voting algorithm
        # when count=0, its time to change the candidate
        # when curr num is diff with candidate, count - 1, otherwise + 1
        # so when count=0, it means current candidate is not the majority number anymore
        # so when count is 0, update candidate with current number
        # 2 2 2 1 1 1 1 2 

        count, candidate = 0, 0
        for num in nums:
            if count == 0: candidate = num
            if num == candidate: 
                count += 1
            else:
                count -= 1
        
        return candidate
