# Last updated: 9/20/2026, 12:53:00 PM
1class Solution:
2    # binary search on answer
3    # 1.fixed totalTrips
4    # 2. return min, time to complete >= totalTrips.  time in range [1, min(time)*totalTrips]
5    # 3. feasible(X): given min time X, can we finish trips >= totalTrips.
6    # the finishedTrips T = sum( X // num for num in time)
7    # 4.return T >= totalTrips
8    def minimumTime(self, time: list[int], totalTrips: int) -> int:
9        def feasible(X:int) -> bool:
10            finished = 0
11            for t in time:
12                finished += X // t
13            
14            return finished >= totalTrips
15        
16        left, right = 1, min(time) * totalTrips
17        res = 0
18        while left <= right:
19            mid = (left + right) // 2
20            if feasible(mid):
21                res = mid
22                right = mid - 1
23            else:
24                left = mid + 1
25        return res