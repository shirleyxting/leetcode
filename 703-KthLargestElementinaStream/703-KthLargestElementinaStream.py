# Last updated: 9/1/2026, 10:29:04 PM
1import heapq
2
3class KthLargest:
4    # min heap of size K
5    def __init__(self, k: int, nums: List[int]):
6        self.k = k
7        self.heap = nums
8
9        heapq.heapify(self.heap)
10
11        while len(self.heap) > self.k:
12            heapq.heappop(self.heap)
13
14
15    def add(self, val: int) -> int:
16        heapq.heappush(self.heap, val)
17
18        if len(self.heap) > self.k:
19            heapq.heappop(self.heap)
20        
21        return self.heap[0]
22        
23
24
25# Your KthLargest object will be instantiated and called as such:
26# obj = KthLargest(k, nums)
27# param_1 = obj.add(val)