# Last updated: 9/16/2026, 4:07:19 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        left, right = 0, len(s) - 1
4
5        while left < right:
6            while left < right and not s[left].isalnum():
7                left += 1
8            while left < right and not s[right].isalnum():
9                right -= 1
10            
11            if s[left].lower() != s[right].lower():
12                return False
13            
14            left += 1
15            right -= 1
16        
17        return True