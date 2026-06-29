# Last updated: 6/28/2026, 9:53:33 PM
1class Solution:
2    # O(N^2)
3    # def lengthOfLongestSubstring(self, s: str) -> int:
4    #     n = len(s)
5    #     if n == 0 or n == 1:
6    #         return n
7
8    #     res = 0
9    #     for i in range(n):
10    #         seen = set()
11    #         seen.add(s[i])
12    #         for j in range(i + 1, n):
13    #             if s[j] in seen:
14    #                 break
15    #             else:
16    #                 seen.add(s[j])
17            
18    #         res = max(res, len(seen))
19    #     return res
20
21    # sliding window
22    # 时间复杂度降到 O(N)。它就像一个可以伸缩的窗口，右边界不断向右扩大，遇到重复字符时，左边界向右缩小
23    # 你原本的代码在遇到重复时，右指针 j 直接 break，然后左指针 i 只往右挪一格，整个内层循环又要重新从头开始构建 seen 集合。
24    # 而滑动窗口的 left 和 right 指针都只向右走一遍，不需要重复做无用功
25    def lengthOfLongestSubstring(self, s: str) -> int:
26        win = set()
27        max_len = 0
28        left = 0 # slide window left side index
29
30        for right in range(len(s)):
31            # 如果右边界的字符重复了，就一直移动左边界并移除集合里的字符，直到不重复
32            while s[right] in win:
33                win.remove(s[left])
34                left += 1
35            
36            # 把当前右边界字符加入集合
37            win.add(s[right])
38            # 更新最大长度
39            max_len = max(max_len, right - left + 1)
40        
41        return max_len
42
43
44
45