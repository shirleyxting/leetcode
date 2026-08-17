# Last updated: 8/17/2026, 3:19:53 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        # sliding window
4
5        count = defaultdict(int)    # char freq in curr window
6        left = 0
7        max_len = 0
8
9        for right, char in enumerate(s):
10            count[char] += 1
11
12            # rep_cnt: cnt of replacing chars = len(window) - max_freq
13            # move rep_cnt to while condition, otherwise rep_cnt is not updating while left +=1
14            while left < right + 1 and (right - left + 1) - max(count.values()) > k:
15                count[s[left]] -= 1
16                left += 1
17            
18            # update res
19            max_len = max(max_len, right - left + 1)
20        return max_len