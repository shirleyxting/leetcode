# Last updated: 8/16/2026, 9:49:01 PM
from collections import defaultdict

class TimeMap:

    def __init__(self):
        # key -> [(timestamp, value)]
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # (ts, value) is sorted -> binary search -> O(logn)
        n = len(self.store[key])
        records = self.store[key] # [(ts, val)]

        res = ""
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if records[mid][0] <= timestamp:
                res = records[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)