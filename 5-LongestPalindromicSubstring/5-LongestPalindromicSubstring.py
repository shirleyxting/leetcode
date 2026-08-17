# Last updated: 8/16/2026, 9:53:56 PM
# DP：从"检查回文"这个动作本身里发现了重复计算 → 缓存更小子问题的答案
# 中心扩展：从"要找的目标"这个对象本身的几何性质（对称）里发现了枚举方式可以更聪明 → 换一种枚举维度（中心而不是端点）
# 这两条路径都能从暴力解法出发想到，只是需要往两个不同的地方"较真"
#   你之前卡住可能是因为想到了DP那条线的重复计算，但没往"回文的对称性"这个角度去想；
#   也可能是反过来。以后遇到类似问题，可以同时问自己这两个问题：
#   "这个检查动作里有没有可复用的子问题？"和"我要找的目标本身有没有特殊几何/结构性质，能不能换个枚举维度？"

# Two ways to optimize from brute force:
# DP: the "check palindrome" action itself has a reusable subproblem -> cache smaller subproblem answers
# Center expansion: the target itself (palindrome) has symmetry -> enumerate centers instead of endpoints
# When stuck, ask: (1) does this check reuse a smaller version of itself? (2) does the target have structure that lets me change what I enumerate over?

# # 1.brute force: O(n^3)
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) <= 1:
#             return s

        # def checkPalindrome(s: str) -> bool:
        #     if len(s) <= 1:
        #         return True
        #     i, j = 0, len(s) - 1
        #     while i < j:
        #         if s[i] != s[j]:
        #             return False
        #         i += 1
        #         j -= 1
            
        #     return True
        
        # def checkPalindrome(s: str) -> bool:
        #     # check if s == reversed s
        #     return s == s[::-1]
            
#         res = ""
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 curr = s[i: j+1]
#                 if checkPalindrome(curr) and len(curr) > len(res):
#                     res = curr
#         return res
        

# 2.DP: O(n^2)
# dp[i][j]: s[i:j+1] is palindorme
#   = (s[i]==s[j] and dp[i+1][j-1])
# class Solution:
#     def longestPalindrome(self, s: str) -> str:    
#         if len(s) <= 1:
#             return s

#         n = len(s)

#         # dp = [[False for _ in range(n)] for _ in range(n)]
#         dp = [[False] * n for _ in range(n)]

#         # single char
#         for i in range(n):
#             dp[i][i] = True
        
#         start = 0   # start index of the longest palindrome
#         max_len = 1 # at this point, we check from L>=2
        
#         for L in range(2, n+1):
#             for i in range(n-L+1):
#                 j = i - 1 + L

#                 if s[i] == s[j]:
#                     if L <= 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i+1][j-1]
#                 else:
#                     dp[i][j] = False
                
#                 if dp[i][j] and L > max_len:
#                     start = i
#                     max_len = L
        
#         return s[start: start + max_len]


# 3. expand from center
# iterate the center, instead of iterate the start/end of the substring
# odd len: n possible centers
# even len: n-1 
# iterate thru 2n-1, instead n^2
class Solution:
    def longestPalindrome(self, s: str) -> str:   
        if len(s) <= 1:
            return s
        
        # expand from l,r, until not palindrome
        def expand(l: int, r: int) -> List[int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            # 循环结束时left/right已经"多走了一步"，实际回文范围是 [left+1, right-1]
            return [l+1, r-1]

        
        start, end = 0, 0  # index for res
        for i in range(len(s)):
            l_o, r_o = expand(i, i)   # for odd len, center is s[i]
            l_e, r_e = expand(i, i+1) # for even len, center is btw s[i] and s[i+1]

            if r_o - l_o > end - start:
                start = l_o
                end = r_o
            if r_e - l_e > end - start:
                start = l_e
                end = r_e
        
        return s[start:end + 1]


