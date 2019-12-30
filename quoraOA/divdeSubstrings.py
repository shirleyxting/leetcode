__author__ = ' Zhen Wang'


class Solution:

    def divide(self, number: int, k: int) -> int:
        s = str(number)
        st = set()
        for i in range(len(s) - k + 1):
            subStr = s[i: i + k]
            num = int(subStr)
            if num != 0 and number % num == 0:
                st.add(num)

        return len(st)


if __name__ == "__main__":
    sol = Solution()
    number = 120
    k = 2
    print(sol.divide(number, k))
