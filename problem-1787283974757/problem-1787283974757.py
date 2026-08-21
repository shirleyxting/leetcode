# Last updated: 8/20/2026, 8:46:14 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        # only lowercase, so use [26] list
4        if len(s) != len(t):
5            return False
6
7        count = [0] * 26
8
9        for c1, c2 in zip(s, t):
10            count[ord(c1) - ord('a')] += 1
11            count[ord(c2) - ord('a')] -= 1
12        
13        return all(c == 0 for c in count)