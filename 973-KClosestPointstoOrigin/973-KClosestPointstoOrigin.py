# Last updated: 9/16/2026, 3:34:38 PM
1class Solution:
2    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
3        # maintain top k smallest dist
4        # max_heap with size = k
5        # min_heap with size = k, and negative dist as values
6        heap = []
7
8        for x, y in points:
9            dist = -(x * x + y * y)
10            heapq.heappush(heap, (dist, x, y))
11
12            if len(heap) > k:
13                heapq.heappop(heap)
14        
15        return [[x, y] for _, x, y in heap]