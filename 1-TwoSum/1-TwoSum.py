# Last updated: 6/27/2026, 10:37:11 PM
1class Solution:
2    # def twoSum(self, nums: List[int], target: int) -> List[int]:
3    #     # brute force
4    #     n = len(nums)
5    #     for i in range(n):
6    #         for j in range(i + 1, n):
7    #             if nums[i] + nums[j] == target:
8    #                 return [i, j]
9        
10    #     return [-1, -1]
11    
12    def twoSum(self, nums: List[int], target: int) -> List[int]:
13        # hashmap
14        # if scan once, for each element, check if visited "target - curr" before
15        # hashmap key = curr, value = index
16        seen = {}
17        n = len(nums)
18        for i in range(n):
19            new_target = target - nums[i]
20            if new_target in seen:
21                return [seen[new_target], i]
22            seen[nums[i]] = i
23            # print(seen)
24        return [-1, -1]
25