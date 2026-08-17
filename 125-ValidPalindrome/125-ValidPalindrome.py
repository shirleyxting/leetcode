# Last updated: 8/16/2026, 9:52:17 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # isalnum: check if its alphanumeric (letter or digit)

        # l = 0
        # r = len(s) - 1
        # while(l < r):
        #     if not s[l].isalnum(): l += 1
        #     elif not s[r].isalnum(): r -= 1
        #     else:
        #         if s[l].lower() == s[r].lower():
        #             l += 1
        #             r -= 1
        #         else:
        #             return False
        
        # return s[l].lower() == s[r].lower()

        # clean the string first
        newS = ''.join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(newS) - 1

        if len(newS) <= 1: return True

        while(l < r):
            if newS[l] != newS[r]: return False
            l += 1
            r -= 1
        
        return newS[l] == newS[r]
