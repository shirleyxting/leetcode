# Last updated: 8/18/2026, 9:07:06 PM
1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        # row_zero[i] (size:m) = true -> matrix[i][0] = 0
7        # col_zero[j] (size:n) = true -> matrix[0][j] = 0
8        # but if 0-row, 0-col has 0, needs to log at first
9
10        m, n = len(matrix), len(matrix[0])
11
12        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
13        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
14
15        # flag 0s using first_row, first_col
16        for i in range(1, m):
17            for j in range(1, n):
18                if matrix[i][j] == 0:
19                    matrix[i][0] = 0
20                    matrix[0][j] = 0
21        
22        # convert flagged rows, cols to 0
23        for i in range(1, m):
24            for j in range(1, n):
25                if matrix[i][0] == 0 or matrix[0][j] == 0:
26                    matrix[i][j] = 0
27        
28        # process first_row and first_col:
29        if first_row_has_zero:
30            for j in range(n):
31                matrix[0][j] = 0
32        if first_col_has_zero:
33            for i in range(m):
34                matrix[i][0] = 0
35
36        return
37
38        