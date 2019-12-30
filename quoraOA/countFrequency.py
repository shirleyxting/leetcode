__author__ = ' Zhen Wang'

from typing import List


class Solution:

    def countFreq(self, array: List[int], matrix: List[List[int]]):
        map = {}

        for i in range(len(array)):
            item = array[i]
            if item not in map:
                map[item] = []
            map[item].append(i)

        rst = 0

        for i in range(len(matrix)):
            l, r, target = matrix[i][0], matrix[i][1], matrix[i][2]
            if target in map:
                for idx in map[target]:
                    if idx >= l and idx <= r:
                        rst += 1

        return rst


if __name__ == "__main__":
    sol = Solution();
    arr = [1, 1, 2, 3, 2]
    matrix = [
        [1, 2, 1],
        [2, 4, 2],
        [0, 3, 1]
    ]
    print(sol.countFreq(arr, matrix))

