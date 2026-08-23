# Last updated: 8/22/2026, 10:51:23 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7# class Solution:
8#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9#         # iteration
10#         stack = []
11#         node = root
12
13#         while stack or node:
14#             # s1: go all the way to the left, until reach the leftmost node (the smallest val)
15#             while node:
16#                 stack.append(node)
17#                 node = node.left
18            
19#             # s2: process curr node
20#             node = stack.pop()
21#             k -= 1
22#             # the kth popped node is kth smallest, return
23#             if k == 0:
24#                 return node.val
25            
26#             # s3: process right subtree
27#             node = node.right
28        
29#         return -1
30
31
32
33# recursion (just for knowledge, iteration version is easier)
34class Solution:
35    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
36        count = 0
37        result = None
38
39        def dfs(node):
40            nonlocal count, result
41
42            # exit check-1
43            if node is None or result is not None:
44                return
45            
46            # process left subtree
47            dfs(node.left)
48
49            # exit-check-2: if result is found in left subtree, no need to proceed root and right subtree
50            if result is not None:
51                return
52            
53            # process root node
54            count += 1
55            if count == k:  # exit check-3
56                result = node.val
57                return
58            
59            # process right subtree
60            dfs(node.right)
61        
62
63        dfs(root)
64        return result
65
66