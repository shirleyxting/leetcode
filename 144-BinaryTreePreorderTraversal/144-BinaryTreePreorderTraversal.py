# Last updated: 9/3/2026, 5:20:34 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        # if not root:
10        #     return []
11        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
12
13        # stack simulate recursion
14        # root-left-right
15        if not root:
16            return []
17        
18        stack = [root]
19        res = []
20
21        while stack:
22            node = stack.pop()
23            res.append(node.val)
24            # push to stack in reversed order: right -> left
25            # so left is at the stack top, next will pop left first
26            if node.right:
27                stack.append(node.right)
28            if node.left:
29                stack.append(node.left)
30        
31        return res
32
33