# Last updated: 9/1/2026, 3:43:09 PM
1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        # start from the end, then reverse
4        i, j = len(a)-1, len(b)-1
5        carry = 0
6        res = []   # list of str of added res, in reverse order
7
8        while i >= 0 or j >= 0 or carry > 0:
9            total = carry   # total will be reset to carry every round
10
11            if i >= 0:
12                total += int(a[i])
13                i -= 1
14            if j >= 0:
15                total += int(b[j])
16                j -= 1
17        
18            total, carry = total % 2, total // 2
19            res.append(str(total))
20        
21        return ''.join(reversed(res))
22