# Last updated: 9/3/2026, 3:09:53 PM
1class SnapshotArray:
2    # global counter: snap_id (always increasing, +1 when call snap())
3    # for each idx, record list of [(snap_id, val), (s2, v2), ...]
4
5    # get() is to find first 'snap_i' <= target_snap_id, in history[idx] list (sorted, ASC for snap_id)
6    # binary search
7    def __init__(self, length: int):
8        self.snap_id = 0
9        # history[i] = [(s1, v1), (s2, v2), ...]
10        # init (0, 0) for every idx
11        self.history = [ [(0, 0)] for _ in range(length) ]
12
13    def set(self, index: int, val: int) -> None:
14        snaps = self.history[index]
15        # snaps is order by snap_id ASC
16        # update the last item (the latest snapshot)
17        if self.snap_id == snaps[-1][0]:
18            # overwrite update curr snapshot
19            snaps[-1] = (self.snap_id, val)
20        else:
21            # only possible: self.snap_id > snaps[-1][0] (as snap_id is increasing)
22            # append new snap_id to the snaps list
23            snaps.append( (self.snap_id, val) )
24
25
26    def snap(self) -> int:
27        self.snap_id += 1   # next snap_id
28        return self.snap_id - 1
29        
30
31    def get(self, index: int, snap_id: int) -> int:
32        # get first snap_i <= target_snap_id
33        # build tuple for comparison: (snap_id, float('inf'))
34        # +inf to ensure > any val
35
36        snaps = self.history[index]
37        snap_idx = bisect.bisect_right(snaps, (snap_id, float('inf')) ) - 1
38
39        return snaps[snap_idx][1]
40        
41
42
43# Your SnapshotArray object will be instantiated and called as such:
44# obj = SnapshotArray(length)
45# obj.set(index,val)
46# param_2 = obj.snap()
47# param_3 = obj.get(index,snap_id)