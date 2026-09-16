# Last updated: 9/15/2026, 10:11:58 PM
1class Allocator:
2
3    # def __init__(self, n: int):
4    #     # 0 means free
5    #     self.memory = [0] * n
6
7    # def allocate(self, size: int, mID: int) -> int:
8    #     free = 0    # so far, count of free blocks
9    #     for i, v in enumerate(self.memory):
10    #         if v == 0:
11    #             free += 1
12    #             if free == size:
13    #                 # [i - free + 1, i]: curr window
14    #                 start = i - free + 1
15    #                 for j in range(start, i + 1):
16    #                     self.memory[j] = mID
17    #                 return start
18    #         else:   # reset curr window
19    #             free = 0
20        
21    #     return -1
22
23    # def freeMemory(self, mID: int) -> int:
24    #     count = 0
25    #     for i, v in enumerate(self.memory):
26    #         if v == mID:
27    #             self.memory[i] = 0
28    #             count += 1
29    #     return count
30
31
32    # if n is very large and cannot be saved upfront
33    # record the allocated blocks: (start, end, mID) for [start, end)
34    def __init__(self, n: int):
35        self.n = n
36        self.blocks = []    # sorted by start
37
38    def allocate(self, size: int, mID: int) -> int:
39        prev_end = 0
40        for i, (start, end, _) in enumerate(self.blocks):
41            if start - prev_end >= size:
42                # found it, allocate: [prev_end, prev_end + size)
43                # insert at i to keep it sorted
44                self.blocks.insert(i, (prev_end, prev_end + size, mID))
45                return prev_end
46            
47            prev_end = end  # check next block
48        
49        # if did not find any GAPs can fill, check the end of the memory
50        if self.n - prev_end >= size:
51            self.blocks.append((prev_end, prev_end + size, mID))
52            return prev_end
53        
54        return -1
55
56    
57    def freeMemory(self, mID: int) -> int:
58        count = 0   # count of blocks should be freed
59        kept = []   # list of blocks should be kept
60
61        for blk in self.blocks:
62            if blk[2] == mID:
63                count += blk[1] - blk[0]
64            else:
65                kept.append(blk)
66        
67        self.blocks = kept
68        return count
69
70
71# Your Allocator object will be instantiated and called as such:
72# obj = Allocator(n)
73# param_1 = obj.allocate(size,mID)
74# param_2 = obj.freeMemory(mID)