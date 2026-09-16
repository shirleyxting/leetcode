# Last updated: 9/16/2026, 12:10:47 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        curr = root
11
12        while curr:
13            if curr.val > p.val and curr.val > q.val:
14                # go to left subtree
15                curr = curr.left
16            elif curr.val < p.val and curr.val < q.val:
17                # go to right
18                curr = curr.right
19            else:
20                return curr
21        
22        return None