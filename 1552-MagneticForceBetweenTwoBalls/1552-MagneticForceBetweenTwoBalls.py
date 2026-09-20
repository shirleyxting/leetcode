# Last updated: 9/20/2026, 1:14:25 PM
1class Solution:
2    # binary search on answer
3    # 1. fixed m
4    # 2. return max of min dist/force, in range of [1, max(position)-min(position]
5    # 3. feasible(X): given min dist = X, can we put m balls in position?
6    #    #balls we can put: T
7    # 4. return T >= m
8    # iterate X for feasible(X): T T T F F 
9    # we need the right most T
10    def maxDistance(self, position: list[int], m: int) -> int:
11        position.sort()
12
13        def feasible(X: int) -> bool:
14            count = 1
15            prev = position[0]
16            for p in position[1:]:
17                if p - prev >= X:
18                    count += 1
19                    prev = p
20            return count >= m
21        
22        left, right = 1, position[-1] - position[0]
23        res = 0
24        while left <= right:
25            mid = (left + right) // 2
26            if feasible(mid):
27                # move right
28                res = mid
29                left = mid + 1
30            else:
31                right = mid - 1
32        return res
33