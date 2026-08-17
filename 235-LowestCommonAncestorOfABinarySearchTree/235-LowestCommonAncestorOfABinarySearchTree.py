# Last updated: 8/16/2026, 9:50:59 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # # p <= LCA <= q
        # curr = root
        # if curr.val == p.val or curr.val == q.val: return curr

        # temp = p
        # if p.val > q.val: 
        #     p = q
        #     q = temp

        # if curr.val >= p.val and curr.val <= q.val: return curr

        # if curr.val > q.val:
        #     return self.lowestCommonAncestor(curr.left, p, q)
        # if curr.val < p.val:
        #     return self.lowestCommonAncestor(curr.right, p, q)

        # return 

        # BFS - inorder traversal, left-root-right
        curr = root
        # if curr.val == p.val or curr.val == q.val: return curr

        minV, maxV = min(p.val, q.val), max(p.val, q.val)
        
        while curr:
            if curr.val >= minV and curr.val <= maxV: return curr
            elif curr.val < minV: curr = curr.right
            else: curr = curr.left
        
        return None
