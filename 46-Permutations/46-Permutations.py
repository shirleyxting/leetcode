# Last updated: 8/23/2026, 1:07:32 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        # backtrack
4        n = len(nums)
5        res = []
6        path = []           # curr path
7        used = [False] * n  # for each idx if its used in path
8       
9        def backtrack(used: list[bool]):
10            if len(path) == n:
11                res.append(path[:])
12                return
13            
14            for i in range(n):
15                if used[i]:
16                    continue
17
18                path.append(nums[i])    # select i
19                used[i] = True
20
21                backtrack(used)
22                
23                path.pop()
24                used[i] = False         # cancel selection i
25
26
27        backtrack(used)
28        return res