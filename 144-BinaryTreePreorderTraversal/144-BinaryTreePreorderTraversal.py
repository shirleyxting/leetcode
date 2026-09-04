# Last updated: 9/3/2026, 5:16:53 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
12