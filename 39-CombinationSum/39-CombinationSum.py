# Last updated: 8/19/2026, 3:10:42 PM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        # backtracking to return ALL possible answers
4        res = []
5        path = []
6
7        def backtrack(start: int, remaining: int):
8            # find combination sum = remaining in candidates[start:]
9            if remaining == 0:
10                res.append(path[:]) # copy path
11                return
12            if remaining < 0:
13                return
14            
15            for i in range(start, len(candidates)):
16                path.append(candidates[i])          # add to curr path
17                backtrack(i, remaining - candidates[i]) # start from i, cause same candidate can be used multiple times
18                path.pop()                          # cancel the adding
19
20        
21        backtrack(0, target)
22
23        return res