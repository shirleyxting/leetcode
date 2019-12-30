__author__ = ' Zhen Wang'
from typing import List


class Solution:

    def countTarget(self, a: List[int], b: List[int], target: int):
        rst = 0

        for A in a:
            for B in b:
                if A + B == target:
                    rst += 1
        return rst

    def findFeature(self, a: List[int], b: List[int], query: List[List[int]]):
        rst: List[int] = []
        for list in query:
            if len(list) == 2:
                target = list[1]
                record = self.countTarget(a, b, target)
                rst.append(record)
            elif len(list) == 3:
                b[list[1] - 1] = list[2]

        return rst


if __name__ == "__main__":
    sol = Solution()

    a = [1, 2, 3]
    b = [3, 4]
    query = [
        [1, 5],
        [1, 1, 1],
        [1, 5]
    ]

    print(sol.findFeature(a, b, query))
