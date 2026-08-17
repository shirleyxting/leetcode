# Last updated: 8/16/2026, 9:53:20 PM
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # res size: max at m+n
        # num1[i] * num2[j] -> res[i+j+1]

        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m):
            for j in range(n):
                res[i + j + 1] += int(num1[i]) * int(num2[j])

        for k in range(m+n-1, 0, -1):
            # / 是浮点数除法，而 // 是整数向下取整除法。
            # 处理数组索引和进位时，我们需要保留整数，如果使用 / 10，结果会变成浮点数（例如 23 / 10 = 2.3）
            res[k - 1] += res[k] // 10
            res[k] %= 10
            
        # discard leading 0 until 1 digit left
        if all(x == 0 for x in res):
            return "0"

        return "".join(map(str, res)).lstrip("0")
