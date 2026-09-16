# Last updated: 9/16/2026, 12:21:27 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        # dfs, record cnt of good nodes so far
10        # pass "max_so_far value" to next layer
11
12        # return count of good nodes
13        def dfs(node, max_so_far: int) -> int:
14            if node is None:
15                return 0
16            
17            good = 1 if node.val >= max_so_far else 0
18
19            new_max = max(node.val, max_so_far)
20
21            return good + dfs(node.left, new_max) + dfs(node.right, new_max)
22        
23        return dfs(root, root.val)