# Last updated: 8/18/2026, 6:44:10 PM
1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        # (i,j) -> (j, n-i-1)
7        # but this one step will overwrite original items
8        # need to split into steps that won't overwrite
9        # (i,j) -> (j,i) -> (j, n-i-1)
10
11        n = len(matrix)
12
13        # transpose
14        for i in range(n):
15            # j starts from i, cause we only transpose HALF matrix
16            # if j starts from 0, we transpose twice, there is no change at the end
17            for j in range(i, n):
18                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
19        
20        # row-level reverse
21        for row in matrix:
22            l, r = 0, n-1
23            while l < r:
24                row[l], row[r] = row[r], row[l]
25                l += 1
26                r -=1
27        
28        return