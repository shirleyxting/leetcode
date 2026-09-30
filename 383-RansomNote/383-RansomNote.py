# Last updated: 9/29/2026, 8:35:33 PM
1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        # if len(ransomNote) > len(magazine):
4        #     return False
5        
6        # stock = Counter(magazine)
7
8        # for c in ransomNote:
9        #     stock[c] -= 1
10        #     if stock[c] < 0:
11        #         return False
12        
13        # return True
14
15        # return Counter(ransomNote) <= Counter(magazine)
16        # return not (Counter(ransomNote) - Counter(magazine) )
17
18        # or only lowercase, use int[26]
19        stock = [0] * 26
20        if len(ransomNote) > len(magazine):
21            return False
22        
23        for c in magazine:
24            stock[ord(c) - ord('a')] += 1
25        
26        for c in ransomNote:
27            idx = ord(c) - ord('a')
28            stock[idx] -= 1
29            if stock[idx] < 0:
30                return False
31        
32        return True