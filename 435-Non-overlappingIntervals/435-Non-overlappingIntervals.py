# Last updated: 9/1/2026, 9:29:40 PM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        # keep most un-overlapping intervals
4        # sort by end, as ending early can give more space for next meetings
5
6        intervals.sort(key = lambda x : x[1])
7        # previous meeting end, compare with curr start
8        prev_end = float('-inf')
9
10        count = 0   # count of removing overlapping 
11
12        for start, end in intervals:
13            if start < prev_end:
14                # overlap, 留 prev（而不是 current）最优：
15                # 因为按 end 排序了 prev.end <= current.end（prev 结束更早）。
16                # 保留结束更早的那个，给后面留的空间更多。
17                count += 1
18            else:
19                # non-overlap
20                prev_end = end
21        
22        return count
23