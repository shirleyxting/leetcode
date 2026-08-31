# Last updated: 8/30/2026, 6:55:17 PM
1class Solution:
2    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
3        # union find
4
5        n = len(edges)  # only 1 extra edge
6        
7        # parent of each node, parent[0] is dummy node
8        parent = list(range(n + 1))
9
10        # find root of each node with path halving acceleration
11        def find(x: int) -> int:
12            while x != parent[x]:
13                parent[x] = parent[parent[x]]
14                x = parent[x]
15            return x
16        
17        # union by rank
18        # return when the first edge cause cycle
19        
20        # rank for each node, rank[0] is dummy
21        rank = [0] * (n + 1)
22
23        for a, b in edges:
24            ra, rb = find(a), find(b)
25            if ra == rb:
26                # current edge a-b has same root, cycle found
27                return [a, b]
28            
29            if rank[ra] < rank[rb]:
30                ra, rb = rb, ra
31            parent[rb] = ra     # hang short tree below tall tree
32            if rank[ra] == rank[rb]:
33                rank[ra] += 1   # same rank for two tree, tall tree + 1
34        
35        return None