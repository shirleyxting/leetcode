# Last updated: 8/17/2026, 9:53:34 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        # find i, j pointers in nums1, nums2
4        # left part: nums1[:i] + nums2[:j]
5        # right part: nums1[i:] + nums2[j:]
6        #  left part length = (m+n+1)//2
7        #  L_max <= R_min
8
9        #  j = (m+n+1)//2 - i
10        #  so iterate i in nums1 using binary search
11
12        if len(nums1) > len(nums2):
13            nums1, nums2 = nums2, nums1
14        # ensure nums1 is shorter
15        # why? this can enusre while iterating i in [0, m], j is also legible
16        #  j = (m+n+1)//2 - i  & m <= n
17        #  i_max = m -> j >= 0
18        #  i_min = 0 -> j <= n
19    
20
21        m, n = len(nums1), len(nums2)
22        half = (m+n+1)//2   # consider odd length
23        lo, hi = 0, m
24
25        while lo <= hi:
26            i = (lo + hi) // 2
27            j = half - i
28
29            # get nums1, nums2 items near i,j indicators
30            left1 = nums1[i-1] if i > 0 else float('-inf')
31            right1 = nums1[i] if i < m else float('inf')
32
33            left2 = nums2[j-1] if j > 0 else float('-inf')
34            right2 = nums2[j] if j < n else float('inf')
35
36            # L_max < R_min
37            if left1 <= right2 and left2 <= right1:
38                # found it!
39                if (m + n) % 2 == 1:    # odd, left half has one more item
40                    return max(left1, left2)
41                else:   # even
42                    return (max(left1, left2) + min(right1, right2)) / 2
43            elif left1 > right2:
44                # nums1 has more items
45                hi = i - 1
46            else:
47                lo = i + 1
48        
49        return None
50            
51
52