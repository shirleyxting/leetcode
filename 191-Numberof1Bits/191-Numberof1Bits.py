# Last updated: 8/31/2026, 10:10:36 PM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        # n & (n-1): clear the rightmost 1
4        # until n = 2^x (only has ONE 1, in leftmost), & (n-1) -> 0
5        count = 0
6        while n != 0:
7            n &= n - 1
8            count += 1
9        
10        return count