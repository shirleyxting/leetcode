# Last updated: 8/29/2026, 9:39:43 PM
1class Solution:
2    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
3        # bellman-ford
4        dist = [float('inf')] * (n + 1)
5        dist[k] = 0
6
7        for _ in range(n - 1):
8            updated = False
9
10            for u, v, w in times:
11                # if u is reacheable & find smaller dist
12                if dist[u] != float('inf') and dist[u] + w < dist[v]:
13                    dist[v] = dist[u] + w
14                    updated = True
15                
16            if not updated:
17                break   # if no update this round, exit
18        
19        # dist[0] is dummy node
20        max_dist = max(dist[1:])
21        
22        return max_dist if max_dist != float('inf') else -1
23