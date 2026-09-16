# Last updated: 9/16/2026, 4:23:52 PM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        # sliding window with fixed len (len(s1))
4        # compare win char counts with s1 char counts, int[26]
5
6        n1, n2 = len(s1), len(s2)
7        if n1 > n2:
8            return False
9
10        need = [0] * 26
11        curr = [0] * 26     # curr window, char counts
12
13        for c in s1:
14            need[ord(c) - ord('a')] += 1
15        
16        for i, c in enumerate(s2):
17            # for i >= n1, add one to curr window-rightside, and remove one from curr window-leftside
18            curr[ord(c) - ord('a')] += 1
19
20            if i >= n1:
21                curr[ord(s2[i - n1]) - ord('a')] -= 1
22            
23            if curr == need:
24                return True
25        
26        return False
27