# Last updated: 8/31/2026, 11:54:08 AM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val = 0, neighbors = None):
5        self.val = val
6        self.neighbors = neighbors if neighbors is not None else []
7"""
8
9from typing import Optional
10class Solution:
11    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
12        # # hashmap as visited set and check if curr node is already cloned
13        # old_to_new = {}     # old_node -> new_node
14
15        # # clone curr, return cloned node
16        # def dfs(curr):
17        #     if curr is None:
18        #         return None
19
20        #     if curr in old_to_new:
21        #         return old_to_new[curr]
22            
23        #     # clone
24        #     copy = Node(curr.val)
25        #     old_to_new[curr] = copy     # mark as visited
26
27        #     for nb in curr.neighbors:
28        #         # add neighbors to copy, recursivly
29        #         copy.neighbors.append( dfs(nb) )
30            
31        #     return copy    
32
33        # return dfs(node)
34
35
36        # BFS
37        if not node:
38            return None
39        
40        # clone start first, old_node -> new_node
41        old_to_new = {node: Node(node.val)}
42        queue = deque([node])
43
44        while queue:
45            curr = queue.popleft()
46            for nb in curr.neighbors:
47                if nb not in old_to_new:
48                    queue.append(nb)
49                    # mark as visited during enqueue
50                    old_to_new[nb] = Node(nb.val)
51        
52                # connect curr's clone with nb's clone
53                old_to_new[curr].neighbors.append( old_to_new[nb] )
54        
55        return old_to_new[node]
56