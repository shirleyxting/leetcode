# Last updated: 8/16/2026, 9:51:04 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 树的递归核心心法 / Core mindset for tree recursion
# 不要在脑子里模拟整棵树怎么变，只想清楚"对一个节点该做什么"，剩下交给递归处理子树
# Don't simulate the whole tree in your head 
# figure out what to do for ONE node, 
# then trust recursion to handle the subtrees

# DFS
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         # DFS exit
#         if not root:
#             return root
        
#         # switch left and right childs
#         root.left, root.right = root.right, root.left
        
#         self.invertTree(root.left)
#         self.invertTree(root.right)

#         return root

# BFS
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            # switch left and right
            node.left, node.right = node.right, node.left
            # add not-None childs to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root


