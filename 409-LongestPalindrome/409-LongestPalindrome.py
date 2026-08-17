# Last updated: 8/16/2026, 9:50:20 PM
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # # get count of every chars
        # # use all EVEN cnt char, all ODD char cnt - 1, at last, insert one random ODD char
        # res = 0
        # allEvenFlag = True
        # map = {}
        # for c in s:
        #     map[c] = map.get(c, 0) + 1
        
        # for key, value in map.items():
        #     if value % 2 == 0:
        #         res += value
        #     else:
        #         res += value - 1
        #         allEvenFlag = False
        
        # if not allEvenFlag: res += 1
        # return res

        # OR, res = 
        # if exist ODD char: len(s) - (count of ODD char - 1)
        # if all EVEN char:  len(s)
        odd_char_set = set()
        for c in s:
            if c in odd_char_set:
                odd_char_set.remove(c)
            else:
                odd_char_set.add(c)

        res = 0
        if not odd_char_set: 
            res = len(s)
        else: 
            res = len(s) - (len(odd_char_set) - 1)

        return res
    


