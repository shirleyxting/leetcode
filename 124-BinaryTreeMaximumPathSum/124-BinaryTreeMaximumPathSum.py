# Last updated: 8/17/2026, 5:37:36 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        # 543. Diameter of Binary Tree -> adding edge weights
10        self.max_sum = float("-inf")  # use self, for dfs update
11
12        # for node's parent,
13        # how much can node contribute:
14        #   only node-leftchild, or node-rightchild are eligible
15        def max_gain(node: Optional[TreeNode]) -> int:
16            if not node:
17                return 0
18            
19            # if < 0, skip
20            left_max = max(max_gain(node.left), 0)
21            right_max = max(max_gain(node.right), 0)
22
23            self.max_sum = max(self.max_sum, left_max + node.val + right_max)
24
25            return node.val + max(left_max, right_max)
26        
27        max_gain(root)
28
29        return self.max_sum
30            