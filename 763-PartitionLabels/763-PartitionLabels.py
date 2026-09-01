# Last updated: 9/1/2026, 4:48:30 PM
1class Solution:
2    def partitionLabels(self, s: str) -> List[int]:
3        # scanline + maintaing a running end
4        # for each char, it occus in [start, end] 
5        # maintain curr_end: for chars in curr window, the rightmost end idx
6        # iterate idx-i, when curr_end == i, all chars are included, CUT
7
8        # char -> last occurrence idx
9        # new idx will overwrite old idx
10        ends = {c: i for i, c in enumerate(s)}
11
12        res = []
13        start, end = 0, 0   # curr window: [start, end]
14        for i, c in enumerate(s):
15            end = max(end, ends[c])
16
17            if i == end: # all chars can be included in curr window
18                res.append(end - start + 1)
19                # update start, as new window will start
20                start = end + 1
21        
22        return res
23