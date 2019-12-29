from typing import List
class Solution:
    def arrayAddDelete(self, arr:List[int]) -> int:
        result = arr[0]
        for i in range(1, len(arr)):
            result += pow(-1, i) * arr[i]
        return result


    def intAddDelete(self, n:int) -> int:
        strN = str(n)
        result = int(strN[0])
        for i in range(1, len(strN)):
            result += pow(-1, i) * int(strN[i])

        return result

test = Solution()
print(test.arrayAddDelete([5,4,3,1,5]))
print(test.intAddDelete(54315))