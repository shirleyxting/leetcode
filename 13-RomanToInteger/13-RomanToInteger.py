# Last updated: 8/16/2026, 9:53:43 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        # roman_map = {
        #     'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 
        #     'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        # }

        # res = 0
        # i = 0

        # while i < len(s):
        #     if i < len(s) - 1 and s[i: i+2] in roman_map:
        #         res += roman_map[s[i: i+2]]
        #         i = i + 2
        #         continue
        #     res += roman_map[s[i]]
        #     i += 1
        
        # return res

        # method-2: if current character s[i] < s[i+1], then distract s[i]
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        res, i = 0, 0
        while i < len(s):
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
                res -= roman_map[s[i]]
            else:
                res += roman_map[s[i]]
            i += 1
        
        return res