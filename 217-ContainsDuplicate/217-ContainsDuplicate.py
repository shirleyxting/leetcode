# Last updated: 8/16/2026, 9:51:06 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) != len(nums)

        # seen: hashset, exit early if find num in seen
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
