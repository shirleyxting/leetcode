# Last updated: 8/23/2026, 12:01:00 PM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        # backtrack
4        if not digits:
5            return []
6        
7        phone = {
8            '2': 'abc', '3':'def', '4': 'ghi', '5': 'jkl', 
9            '6': 'mno', '7':'pqrs', '8': 'tuv', '9':'wxyz'
10        }
11        res = []
12        path = []   # curr path
13
14        # get legit path starting from digits[idx]
15        def backtrack(idx: int):
16            # exit: all digits used, then return
17            if len(path) == len(digits):
18                res.append(''.join(path))
19                return
20            
21            # latters mapping to the curr idx
22            letters = phone[digits[idx]]
23            for c in letters:
24                path.append(c)      # select letter from current digit
25                backtrack(idx + 1)  # process next digit
26                path.pop()          # cancel selection
27
28        backtrack(0)
29        return res