__author__ = ' Zhen Wang'


class Solution:

    def check(self, a: str, b: str) -> bool:
        if a is None and b is None:
            return True

        if a is None or b is None:
            return False

        if len(a) != len(b):
            return False

        map_a = {}
        map_b = {}

        for c in a:
            map_a[c] = map_a[c] + 1 if c in map_a else 1

        for c in b:
            map_b[c] = map_b[c] + 1 if c in map_b else 1

        for k in map_a:
            if k not in map_b:
                return False

        count_a = {}
        count_b = {}

        for k in map_a:
            count_a[k] = count_a[k] + 1 if k in count_a else 1

        for k in map_a:
            count_b[k] = count_b[k] + 1 if k in count_b else 1

        for k in count_a:
            if count_a[k] != count_b[k]:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()

    a = "babzccc"
    b = "abbzczz"

    print(sol.check(a, b))

