__author__ = ' Zhen Wang'
from typing import List


class Solution:

    def checkDiff(self, diff: int, a: List[int]):
        for num in a:
            if (num - a[0]) % diff != 0:
                return False
        return True

    def countMaxArithLen(self, a: List[int], b: List[int]):
        st = set()
        for num in a:
            st.add(num)
        a = sorted(a)
        b = sorted(b)

        diffs = []
        if len(a) > 1 and self.checkDiff(a[1] - a[0], a):
            diffs.append(a[1] - a[0])

        r = a[1] if len(a) > 1 else float('inf')
        for num in b:
            if num > a[0] and num < r:
                if self.checkDiff(num - a[0], a):
                    diffs.append(num - a[0])
            if num >= r:
                break

        if len(diffs) == 0:
            return -1

        set_b = set()
        for num in b:
            set_b.add(num)

        maxInsertNum = -1
        minimum, maximum = min(a[0], b[0]), max(a[len(a) - 1], b[len(b) - 1])
        for diff in diffs:
            start, end = a[0] - diff * (a[0] - minimum)//diff, a[0] + diff * (maximum - a[0]) // diff
            endIdx = (a[len(a) - 1] - a[0])//diff
            insertNum = 0
            for i in range(endIdx):
                if (a[0] + i * diff) not in st:
                    if (a[0] + i * diff) not in set_b:
                        break
                    else:
                        insertNum += 1
            idx = 1
            while a[0] - idx * diff >= start:
                tmp = a[0] - idx * diff
                if tmp not in st and tmp in set_b:
                    insertNum += 1
                else:
                    break
                idx += 1

            idx = 1
            while a[len(a) - 1] + idx * diff <= end:
                tmp = a[len(a) - 1] + idx * diff
                if tmp not in st and tmp in set_b:
                    insertNum += 1
                else:
                    break
                idx += 1
            if maxInsertNum < insertNum:
                maxInsertNum = insertNum
        return maxInsertNum + len(a)


sol = Solution()
a = [0, 4, 8, 16]
b = [0,2,4,12,14,20]
a = [7, 13]
b = [1, 10, 16]
a = [20,22]
b = [19, 21,23,24,26,28]
print(sol.countMaxArithLen(a, b))


