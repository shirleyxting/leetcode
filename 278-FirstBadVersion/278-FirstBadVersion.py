# Last updated: 8/16/2026, 9:50:45 PM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # # better than O(n) -> O(logN), binary search, its oooxxxx, find fisrt 'x'
        # l, r = 1, n
        # res = n + 1  # init res to some number larger than n
        # while l + 1 < r: 
        #     # while l < r will lead to endless loop:
        #     # res=4 l=3 r=4
        #     mid = l + (r - l) // 2 
        #     # // integer division
        #     if isBadVersion(mid): 
        #         res = min(res, mid)
        #         r = mid
        #     else: 
        #         l = mid
        #     print(f"res={res} l={l} r={r}")
        
        # if isBadVersion(l):
        #     res = min(res, l)
        # if isBadVersion(r):
        #     res = min(res, r)
        
        # return res

        # no need for res, as the pointer will point to first x
        l, r = 1, n
        while l + 1 < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid): 
                r = mid
            else:
                l = mid
        
        if isBadVersion(l): return l
        if isBadVersion(r): return r
        return -1
