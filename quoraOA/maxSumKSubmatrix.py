from typing import List
import numpy as np

class Solution:
    def maxSumSubmatrix_np(self, matrix:List[List[int]], k:int) -> int:
        """
        find "k*k" sub-matrices in matrix.
        compute the sum of values in k*k sub-matrix, find the max sum
        add the distinct values in ALL POSSIBLE sub-matrices with same "max sum"
        return the add of distinct values

        eg:          k*k             sum: 1+2+4+2 = 2+3+2+2 = 9
        [[1 2 3]    [[1 2]  [[2 3]      return : 1+2+3+4 = 10
         [4 2 2]]   [4 2]]   [2 2]]
        """
        if matrix == None or k <= 0 or len(matrix) < k or len(matrix[0]) < k:
            return -1

        matrix = np.array(matrix)
        num_row, num_col = matrix.shape[0], matrix.shape[1]

        # initialize sums array
        # sums = [[0 for i in range(num_col - k + 1)] for j in range(num_row - k + 1)]
        sum_row = num_row - k + 1
        sum_col = num_col - k + 1
        sums = np.zeros([sum_row, sum_col])

        for i in range(sum_row):
            for j in range(sum_col):
                sums[i][j] = np.sum(matrix[i:i+k, j:j+k])

        locs = np.argwhere(sums == np.max(sums))
        unique_vals = []
        for loc in locs:
            i, j = loc
            unique_vals += np.unique(matrix[i:i+k, j:j+k]).tolist()

        result = sum(set(unique_vals))

        return result


    def maxSumSubmatrix(self, matrix:List[List[int]], k:int) -> int:

        if matrix == None or k <= 0 or len(matrix) < k or len(matrix[0]) < k:
            return -1

        num_row, num_col = len(matrix), len(matrix[0])

        # initialize sums array
        sum_row = num_row - k + 1
        sum_col = num_col - k + 1
        sums = [[0 for i in range(sum_col)] for j in range(sum_row)]

        tmp = 0

        for i in range(sum_row):
            for j in range(sum_col):
                for kk in range(k):
                    sums[i][j] += sum(matrix[i+kk][j:j+k])

        locs = np.argwhere(sums == np.max(sums))
        unique_vals = []
        for loc in locs:
            i, j = loc
            unique_vals += np.unique(matrix[i:i+k, j:j+k]).tolist()

        result = sum(set(unique_vals))

        return result





test = Solution()
print(test.maxSumSubmatrix(
    [[1,2,3,4,1],
     [4,2,2,3,2],
     [3,1,1,2,2],
     [2,1,1,0,2]],
    3))
print(test.maxSumSubmatrix_np(
    [[1,2,3,4,7],
     [4,2,2,3,8],
     [3,11,9,2,2],
     [2,1,2,0,2]],
    3))