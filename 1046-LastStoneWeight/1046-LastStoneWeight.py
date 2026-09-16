# Last updated: 9/16/2026, 3:49:47 PM
1class Solution:
2    def lastStoneWeight(self, stones: list[int]) -> int:
3        # order does not matter
4        # maxheap: pop twice to get maxs, then push once (whats left from collision)
5        heap = [-s for s in stones]
6        heapq.heapify(heap)
7
8        while len(heap) > 1:
9            a = -heapq.heappop(heap) # most heavy
10            b = -heapq.heappop(heap) # sec most heavy
11            if a == b:
12                continue
13            else:
14                heapq.heappush(heap, -(a - b))
15        
16        return -heap[0] if heap else 0