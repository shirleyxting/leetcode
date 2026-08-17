# Last updated: 8/16/2026, 9:50:49 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # only lowercase letters, so only 26 possibilities
        chars = [0] * 26

        for char in s:
            chars[ord(char) - ord('a')] += 1
        
        for char in t:
            chars[ord(char) - ord('a')] -= 1

        for num in chars:
            if num != 0:
                return False
        
        return True