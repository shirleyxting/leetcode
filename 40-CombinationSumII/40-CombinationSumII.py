# Last updated: 8/23/2026, 5:22:28 PM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        # sort, then backtrack, skip same elements in curr selection
4        candidates.sort()
5        res = []
6        path = []   # curr path
7
8        # find combinations sum = remaining from cadidates[start:]
9        def backtrack(start: int, remaining: int):
10            if remaining == 0:
11                res.append(path[:]) # copy of path as path is changing
12                return
13
14            for i in range(start, len(candidates)):
15                # if canidates[start:] evey num > remaining, exit early
16                if remaining - candidates[i] < 0:
17                    break
18
19                # skip same num in current path selection
20                if i > start and candidates[i] == candidates[i-1]:
21                    continue
22
23                # select candidate
24                path.append(candidates[i])
25                # start from i + 1 (same candidate cannot be reused)
26                backtrack(i + 1, remaining - candidates[i])
27                # cancel selection
28                path.pop()
29        
30        backtrack(0, target)
31        return res