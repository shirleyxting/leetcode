# Last updated: 8/16/2026, 9:50:26 PM
class Solution:
    def countBits(self, n: int) -> List[int]:
    #     # n = 5, return [0, 1, 1, 2, 1, 2]
    #     # 0 --> 0
    #     # 1 --> 1
    #     # 2 --> 10
    #     # 3 --> 11
    #     # 4 --> 100
    #     # 5 --> 101
    #     # 6/2 = 3..0, 3/2=1..1 , 1/2=0..1 -> 110

    #     # countBits(n) = countBits(n-1) + number of 1s for n
    #     if n < 0: return []
    #     # base case
    #     if n == 0: return [0]

    #     res = self.countBits(n - 1)

    #     binary_n = self.binaryCountOne(n)

    #     res.append(binary_n)

    #     return res
    
    # # count the number of "1"s in the binary representation of n
    # def binaryCountOne(self, n: int) -> int:
    #     if n == 0: return 0
    #     cnt = 0

    #     while n > 0:
    #         if n % 2 == 1: 
    #             cnt += 1
    #         n = n // 2
        
    #     return cnt

        '''
        method-2
        find relationship for binary representations: i, 2i, 2i+1
        2i = i append '0' at the end
        2i+1 = i append '1' at the end
        0,1,2,3,4,5,6,7,8
        dp[2i] = dp[i]
        dp[2i+1] = dp[i] + 1
        '''
        if n == 0: return [0]
        
        dp = [0] * (n+1)
        # init dp array
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i // 2] + 1
        
        return dp
