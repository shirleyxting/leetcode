# Last updated: 8/16/2026, 9:52:52 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # convert to one dimension list, then binary search
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            r, c = divmod(mid, n)
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False