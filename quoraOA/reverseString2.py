__author__ = ' Zhen Wang'
# leetcode 541

class Solution:

    def reverseStr(self, s: str, k: int):
        a = list(s)
        for start in range(0, len(a), 2 * k):
            i, j = start, min(start + k -1, len(a) - 1)
            while i < j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        return ''.join(a)


sol = Solution()

s = "12345"
k = 2
print(sol.reverseStr(s, k))
