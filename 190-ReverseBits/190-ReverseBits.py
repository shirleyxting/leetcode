# Last updated: 9/1/2026, 3:12:58 PM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        # n right shift, get last digit (n & 1)
4        # res add last digit, res left shift
5
6        res = 0
7        for _ in range(32):
8            res = (res << 1) | (n & 1)
9            n >>= 1
10        
11        return res