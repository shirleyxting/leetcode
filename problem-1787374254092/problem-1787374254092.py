# Last updated: 8/21/2026, 9:50:54 PM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        # wordDict: each word can be selected multiple times -> complete knapsack
4        # dp[j]: for entire wordDict, if word combination = s[:j] (not include char at index j)
5        #      -> for every word, if can find combination = dp[j - word]
6        #      = any(dp[j - len(word)] for word in words )
7        #        j >= len(word) AND s[j-len(word) : j] == word
8        n = len(s)
9        dp = [False] * (n + 1)
10        dp[0] = True    # do not pick any word -> satisfy "" empty string
11
12        for j in range(1, n + 1):
13            dp[j] = any(
14                dp[j - len(word)]
15                for word in wordDict
16                if j >= len(word) and s[j - len(word) : j] == word
17            )
18
19        return dp[n]