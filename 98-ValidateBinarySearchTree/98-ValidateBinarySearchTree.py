# Last updated: 8/16/2026, 9:52:37 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # all left < root < all right
        # left max < root < right min
        # DFS to track left_max, right_min

        def dfs(node: Optional[TreeNode], low, high) -> bool:
            # dfs exit
            if not node:
                return True
            # if not (low < node.val < high):
            #     return False
            
            return (low < node.val < high) and dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        # init range: float('-inf'), float('inf')：
        # no constrainits for root node, use -inf, and inf for always satisfy
        return dfs(root, float('-inf'), float('inf'))