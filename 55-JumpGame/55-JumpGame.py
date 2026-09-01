# Last updated: 9/1/2026, 4:23:27 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        # greedy
4        farthest = 0    # the farthest idx we can reach so far
5
6        for i, num in enumerate(nums):
7            if farthest < i:
8                # if cannot reach current idx, exit
9                return False
10            else:
11                farthest = max(farthest, i + nums[i])
12
13                if farthest >= len(nums) - 1:
14                    return True
15
16        return True