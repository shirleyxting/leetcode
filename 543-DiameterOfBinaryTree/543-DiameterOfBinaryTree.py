# Last updated: 8/16/2026, 9:50:09 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter that CROSS 'root' 
        #  = left.depth - 1 + 1(edge: left-root) 
        #    + right.depth - 1 + 1(edge: right-root)
        # depth(root) = max(depth(left), depth(right)) + 1
        if not root: return 0

        self.max_diameter = 0

        self.findDepth(root)

        return self.max_diameter
    
    def findDepth(self, node: Optional[TreeNode]) -> int:
        # return the depth of a Tree rooted at "Node"

        # recursion exit
        if not node: return 0
        if not node.left and not node.right: return 1

        left_depth = self.findDepth(node.left)
        right_depth = self.findDepth(node.right)

        # while iterating nodes, keep updating the max_diameter
        self.max_diameter = max(left_depth + right_depth, self.max_diameter)

        return max(left_depth, right_depth) + 1


        