# Last updated: 9/30/2026, 4:51:15 PM
1class Solution:
2    def longestCommonPrefix(self, strs: list[str]) -> str:
3        first = strs[0]
4        for i, c in enumerate(first):
5            for s in strs[1:]:
6                if i == len(s) or c != s[i]:
7                    return first[:i]
8        
9        return first
10                