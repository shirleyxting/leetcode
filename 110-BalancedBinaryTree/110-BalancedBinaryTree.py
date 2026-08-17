# Last updated: 8/16/2026, 9:52:20 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # isBalanced(root) = isBalanced(left) & isBalanced(right) & |left.height - right.height| <= 1
        # dfs return both height & isbalanced (-1: not balanced)
        if not root:
            return True

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            # if dfs(node.left) == -1 or dfs(node.right) == -1:
            #     return -1
            # if abs(dfs(node.left) - dfs(node.right)) > 1:
            #     return -1
            # return max(dfs(node.left), dfs(node.right)) + 1

            # use variable to save dfs(node.left) and dfs(node.right), otherwise, there will be multiple calls
            left_height, right_height = dfs(node.left), dfs(node.right)

            if left_height == -1 or right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1

        return dfs(root) != -1