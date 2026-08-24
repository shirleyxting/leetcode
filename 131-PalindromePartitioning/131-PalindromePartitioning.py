# Last updated: 8/23/2026, 5:46:06 PM
1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3        # 1. selection list: from 'start', try all possible cuts for 'end'
4        # 2. when to record/exit: start == len(s), i.e. reach to the end
5        # 3. how to update next level: from 'end' to continuely find cuts -> backtrack(end)
6        # 4. Undo: undo the cut
7
8        res = []
9        path = []
10        n = len(s)
11
12        def is_palindrome(s: str) -> bool:
13            return s == s[::-1]
14
15        def backtrack(start: int):
16            if start == n:
17                res.append(path[:]) # copy path, as path is changing
18            
19            for end in range(start + 1, n + 1):
20                sub = s[start: end]
21                if is_palindrome(sub):
22                    # select cut
23                    path.append(sub)
24                    backtrack(end)
25                    # undo 
26                    path.pop()
27        
28        backtrack(0)
29        return res