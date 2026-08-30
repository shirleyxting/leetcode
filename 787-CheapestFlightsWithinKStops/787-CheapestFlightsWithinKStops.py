# Last updated: 8/29/2026, 10:20:26 PM
1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        # prices[i]: the min price from src to i (based on curr visited paths)
4        # 'inf' means so far, does not know any path can go to this node
5        prices = [float('inf')] * n
6        prices[src] = 0
7
8        # at most k stops -> at most k+1 nodes -> at most k+1 rounds of 'relax'
9        for _ in range(k + 1):
10            # use prev round dist to update curr dist
11            #   ensure each round, only move one step
12            #   updates in curr round, cannot be reused
13            curr = prices[:]
14
15            for u, v, w in flights:
16                if prices[u] != float('inf') and prices[u] + w < curr[v]:
17                    curr[v] = prices[u] + w
18            
19            prices = curr
20        
21        return prices[dst] if prices[dst] != float('inf') else -1
22