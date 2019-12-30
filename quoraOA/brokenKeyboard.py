__author__ = ' Zhen Wang'

from typing import List


class Solution:

    def numOfWords(self, s: str, keys: List[str]) -> int:

        if s is None or len(s) == 0:
            return 0

        st = set()

        for key in keys:
            st.add(key)

        words = s.split(" ")

        rst = 0

        for word in words:
            flag = True;
            for c in word:
                if c.isalpha() and c not in st:
                    flag = False
                    break
            if flag:
                rst += 1

        return rst


if __name__ == "__main__":
    sol = Solution();
    # s = "hello, world"
    # keys = ["i", "e", "o", "l", "h"]
    # print(sol.num_of_words(s, keys))

    s = "1 + 2 = 3"
    k = []
    print(sol.numOfWords(s, k))



