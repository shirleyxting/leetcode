# Last updated: 8/16/2026, 9:50:22 PM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        map = [0] * 26

        for c in magazine:
            map[ord(c) - ord('a')] += 1
        
        for c in ransomNote:
            map[ord(c) - ord('a')] -= 1
            if map[ord(c) - ord('a')] < 0: return False
        
        return True

