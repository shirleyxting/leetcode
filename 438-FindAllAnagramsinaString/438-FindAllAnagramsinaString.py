# Last updated: 9/30/2026, 5:28:40 PM
1class Solution:
2    def findAnagrams(self, s: str, p: str) -> list[int]:
3        # iterate all window with length of p
4        # win's counter = p's counter
5
6        n = len(p)
7        need = [0]* 26
8        for c in p:
9            need[ord(c) - ord('a')] += 1
10        
11        win = [0] * 26
12        left = 0
13        res = []
14        # win: [left, right), win_len = right - left
15        for right, c in enumerate(s, 1):
16            win[ord(c) - ord('a')] += 1
17
18            if right - left > n:
19                # win length > n, shrink left
20                win[ord(s[left]) - ord('a')] -= 1
21                left += 1
22            
23            if right - left == n and win == need:
24                res.append(left)
25        
26        return res