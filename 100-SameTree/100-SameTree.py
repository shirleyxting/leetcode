# Last updated: 9/16/2026, 11:58:00 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
9        if not p and not q:
10            return True
11        
12        if not p or not q or p.val != q.val:
13            return False
14        
15        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)