# Last updated: 8/16/2026, 9:52:31 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # DFS: maxDepth(root) = max( maxDep(left), maxDepth(right) ) + 1
        # if not root: return 0

        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # BFS
        if not root: return 0
        queue = deque()
        queue.append(root)
        depth = 0

        while queue:
            depth += 1
            # process nodes level by level
            # process nodes in current level
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        return depth