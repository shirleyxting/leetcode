# Last updated: 8/17/2026, 5:06:51 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        # res = max(left_depth + right_depth)
10        # dfs to get tre depth, and update global variable 'res'
11
12        max_diameter = 0
13
14        def height(node: Optional[TreeNode]) -> int:
15            nonlocal max_diameter # ensure max_diameter is read from global
16            
17            if not node:
18                return 0
19            
20            l_h = height(node.left)
21            r_h = height(node.right)
22
23            max_diameter = max(max_diameter, l_h + r_h)
24
25            return max(l_h, r_h) + 1
26        
27        height(root)
28
29        return max_diameter