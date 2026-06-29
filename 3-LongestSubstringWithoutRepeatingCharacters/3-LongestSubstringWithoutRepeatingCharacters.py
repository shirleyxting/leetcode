# Last updated: 6/28/2026, 9:39:13 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        n = len(s)
4        if n == 0 or n == 1:
5            return n
6
7        res = 0
8        for i in range(n):
9            seen = set()
10            seen.add(s[i])
11            for j in range(i + 1, n):
12                if s[j] in seen:
13                    break
14                else:
15                    seen.add(s[j])
16            
17            res = max(res, len(seen))
18        
19        return res
20
21