# Last updated: 9/17/2026, 9:34:56 PM
1class Solution:
2    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
3        # 1. given k adjacent flowers, m bouquets
4        # 2. need the min days to make m bouquets, min_days in range [min(bloomDay), max(bloomDay)]
5        # 3. feasible(X): given X days, k adjacent flowers, get the number of bouquets you can make -> T
6        # 4. return m <= T
7        #   larger X -> larger T, so feasible() is monotonic
8        #   iterate min_days in [min(bloomDay), max(bloomDay)]: we will get: F F T T T 
9        #   we need the leftmost T
10
11        def feasible(X: int) -> bool:
12            # curr: curr flower count, b_count: count of bouquets made
13            curr, b_count = 0, 0
14            for day in bloomDay:
15                if day <= X:
16                    curr += 1
17                    if curr == k:
18                        b_count += 1
19                        curr = 0
20                else:
21                    curr = 0
22            return m <= b_count
23        
24        left, right = min(bloomDay), max(bloomDay)
25        res = 0
26        while left <= right:
27            mid = (left + right) // 2
28            if feasible(mid):
29                res = mid
30                right = mid - 1
31            else:
32                left = mid + 1
33        
34        return res if res > 0 else -1
35
36