# Last updated: 9/16/2026, 12:06:04 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
9        
10        def isSameTree(p, q) -> bool:
11            if p is None and q is None:
12                return True
13            if p is None or q is None or p.val != q.val:
14                return False
15            
16            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
17        
18        if subRoot is None:
19            return True
20        
21        if root is None and subRoot is not None:
22            return False
23        
24        if isSameTree(root, subRoot):
25            return True
26        
27        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)