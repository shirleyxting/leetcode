# Last updated: 9/1/2026, 8:28:58 PM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        # [s1, e1] for every interval, [s2,e2]: new_interval
4        # leftside of new:          e1 < s2
5        # overlap, need combine:    e1 >= s2 & s1 <= e2
6        # rightside of new:         s1 > e2
7
8        i, n = 0, len(intervals)
9        s2, e2 = newInterval[0], newInterval[1]
10
11        res = []
12
13        # leftside, copy directly
14        while i < n and intervals[i][1] < s2:
15            res.append(intervals[i])
16            i += 1
17        
18        # update [s2,e2] when overlapping
19        while i < n and intervals[i][0] <= e2:
20            s2 = min(intervals[i][0], s2)
21            e2 = max(intervals[i][1], e2)
22            i += 1
23        res.append([s2, e2])
24
25        # rightside, copy directly
26        while i < n:
27            res.append(intervals[i])
28            i += 1
29        
30        return res
31
32            
33
34