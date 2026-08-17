# Last updated: 8/17/2026, 12:05:59 PM
1from collections import Counter
2
3class Solution:
4    def minWindow(self, s: str, t: str) -> str:
5        # slide window
6        # for fixed left, find right to ensure all chars in t
7        # then left += 1, to find next window
8
9        if not s or not t:
10            return ""
11        
12        need = Counter(t)   # for char in t, how much is still required
13        missing = len(t)    # how much is missing (just number)
14
15        left = 0                        # curr window left
16        best_left, best_right = 0, 0    # record the best window [left, right]
17        found = False                   # flag for curr window satifying all chars in t
18
19        # need[char] < 0: means char is not necessary, can be discarded
20        for right, char in enumerate(s):
21            if need[char] > 0:  # found a necessary char
22                missing -= 1
23            
24            need[char] -= 1     # update need, no matter if char is necessary or not
25
26            # if found "all chars in t"
27            if missing == 0:
28                # shrink left (need[left] < 0 ensure left can be abandoned)
29                # left < right+1: ensure still in window [left, right]
30                while left < right + 1 and need[s[left]] < 0:
31                    need[s[left]] += 1
32                    left += 1
33                
34                # update best_window
35                if not found or right - left + 1 < best_right - best_left + 1:
36                    found = True
37                    best_left, best_right = left, right
38                
39                # remove necessary left from the curr window, and left + 1 to search next win
40                need[s[left]] += 1
41                missing += 1
42                left += 1
43        
44        return s[best_left: best_right + 1] if found else ""
45
46
47            
48
49            
50
51