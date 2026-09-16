# Last updated: 9/15/2026, 9:42:32 PM
1class Allocator:
2
3    def __init__(self, n: int):
4        # 0 means free
5        self.memory = [0] * n
6
7    def allocate(self, size: int, mID: int) -> int:
8        free = 0    # so far, count of free blocks
9        for i, v in enumerate(self.memory):
10            if v == 0:
11                free += 1
12                if free == size:
13                    # [i - free + 1, i]: curr window
14                    start = i - free + 1
15                    for j in range(start, i + 1):
16                        self.memory[j] = mID
17                    return start
18            else:   # reset curr window
19                free = 0
20        
21        return -1
22
23    def freeMemory(self, mID: int) -> int:
24        count = 0
25        for i, v in enumerate(self.memory):
26            if v == mID:
27                self.memory[i] = 0
28                count += 1
29        return count
30        
31
32
33# Your Allocator object will be instantiated and called as such:
34# obj = Allocator(n)
35# param_1 = obj.allocate(size,mID)
36# param_2 = obj.freeMemory(mID)