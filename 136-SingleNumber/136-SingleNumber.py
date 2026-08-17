# Last updated: 8/16/2026, 9:52:09 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # seen = set()

        # for num in nums:
        #     if num not in seen:
        #         seen.add(num)
        #     else:
        #         seen.remove(num)
        # res = 0
        # for num in seen:
        #     res = num
        # return res

        # # method 2: ordering
        # # 1 1 2 3 3
        # # 1 1 2 2 3
        # nums.sort()
        # i = 0
        # res = 0
        # while i < len(nums) - 1:
        #     if nums[i] == nums[i + 1]:
        #         i += 2
        #     else:
        #         res = nums[i]
        #         break
        # if i == len(nums) - 1: 
        #     return nums[i]
        # return res

        # method 3: bitwise XOR
        # 0^a=a, a^a=0, a^a^a=a
        # a^b^c^a^c = a^a^c^c^b  = 0^b = b
        res = 0
        for num in nums:
            res ^= num
        
        return res

            
