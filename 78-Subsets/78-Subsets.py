# Last updated: 8/23/2026, 11:32:16 AM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        # backtrack
4        res = []
5        path = []   # current path
6
7        # find subsets in nums[start:]
8        def backtrack(start: int):
9            # every path is legit
10            res.append(path[:])     # copy of path (cause path is changing)
11
12            for i in range(start, len(nums)):
13                path.append(nums[i])
14                backtrack(i + 1)    # num cannot be reused, so next is i+1
15                # cancel
16                path.pop()
17
18
19        backtrack(0)
20        return res