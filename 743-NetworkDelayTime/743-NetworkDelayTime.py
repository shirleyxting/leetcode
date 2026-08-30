# Last updated: 8/29/2026, 10:02:34 PM
1class Solution:
2    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
3        # # bellman-ford
4        # dist = [float('inf')] * (n + 1)
5        # dist[k] = 0
6
7        # for _ in range(n - 1):
8        #     updated = False
9
10        #     for u, v, w in times:
11        #         # if u is reacheable & find smaller dist
12        #         if dist[u] != float('inf') and dist[u] + w < dist[v]:
13        #             dist[v] = dist[u] + w
14        #             updated = True
15                
16        #     if not updated:
17        #         break   # if no update this round, exit
18        
19        # # dist[0] is dummy node
20        # max_dist = max(dist[1:])
21
22        # return max_dist if max_dist != float('inf') else -1
23
24
25        # Dijkstra, minHeap, greedy on every min dist of un-confirmed nodes
26        graph = defaultdict(list)   # u -> (v1,w1), (v2,w2), ...
27        for u, v, w in times:
28            graph[u].append((v, w))
29        
30        # dist[0] is dummy node
31        dist = [float('inf')] * (n + 1)
32        dist[k] = 0     # start node dist = 0
33
34        visited = set()
35
36        heap = [(0, k)]     # heap: (dist of the node, node), min_heap order by dist
37        while heap:
38            # greedy to pick min_dist of un-confirmed nodes
39            d, u = heapq.heappop(heap)
40            if u in visited:    # skip outdated nodes
41                continue
42            visited.add(u)
43
44            # update u's adjacent nodes dist
45            for v, w in graph[u]:
46                # dist[u] + w < dist[v], and dist[u] = d
47                if v not in visited and d + w < dist[v]:
48                    dist[v] = d + w
49                    heapq.heappush(heap, (dist[v], v))
50        
51        max_dist = max(dist[1:])    # dist[0] is dummy node
52
53        return max_dist if max_dist != float('inf') else -1
54
55
56
57
58
59