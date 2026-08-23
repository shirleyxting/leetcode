# Last updated: 8/22/2026, 10:44:52 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        # iteration
10        stack = []
11        node = root
12
13        while stack or node:
14            # s1: go all the way to the left, until reach the leftmost node (the smallest val)
15            while node:
16                stack.append(node)
17                node = node.left
18            
19            # s2: process curr node
20            node = stack.pop()
21            k -= 1
22            # the kth popped node is kth smallest, return
23            if k == 0:
24                return node.val
25            
26            # s3: process right subtree
27            node = node.right
28        
29        return -1
30            
31
32