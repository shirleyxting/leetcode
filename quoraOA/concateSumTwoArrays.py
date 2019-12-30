__author__ = ' Zhen Wang'

from typing import List


class Solution:

    def sum(self, a: List[int], b: List[int]) -> int:
        rst = 0

        if len(a) != len(b):
            return rst

        for i in range(len(a)):
            rst += self.concatenate(a[i], b[len(b) - i - 1])

        return rst

    def concatenate(self, n1: int, n2: int) -> int:
        i = 1

        while n2 != 0:
            n1 = n1 * 10 + n2 % 10 * i
            n2 //= 10
            i += 1

        return n1


if __name__ == "__main__":
    sol = Solution()

    a = [12, 3]
    b = [1, 2]

    print(sol.sum(a, b))

