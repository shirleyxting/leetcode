# Last updated: 8/16/2026, 9:51:38 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        # '''
        # 0-0
        # 1-1
        # 2-1 (1*2, 1)
        # 3-2 (1*2+1, 1+1)
        # 4-1 (2*2, 1)
        # 5-2 (2*2+1, 1+1)
        # 6-2 (3*2, 2)
        # 7-3 (3*2+1, 2+1) 111 4+2+1
        # 8-1 (4*2, 1)1000
        # 9-2 (4*2+1, 1+1)
        # 10-2 (5*2, 2)
        # 11-3 (5*2+1, 2+1) 1011 ... (2*2+1)*2+1 
        # 12-2
        # 13-3
        
        # f(n) = f(n/2),     if n is even
        #      = f(n/2) + 1, if n is odd
        # '''

        # if n == 0 or n == 1: return n
        # if n % 2 == 0:
        #     return self.hammingWeight(n // 2)
        # else:
        #     return self.hammingWeight(n // 2) + 1
        
        # return -1

        # method2 n&1, get the last digit is 1 or not, then right shift n by 1 bit
        res = 0
        while n:
            res += n & 1
            n = n >> 1
        
        return res

