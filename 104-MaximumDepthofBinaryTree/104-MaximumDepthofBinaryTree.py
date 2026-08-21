# Last updated: 8/20/2026, 8:52:58 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        # if not root:
10        #     return 0
11        
12        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
13
14
15        # BFS
16        if not root:
17            return 0
18        
19        queue = deque([root])
20        res = 0
21
22        while queue:
23            # level order traversal
24            q_size = len(queue)
25            for _ in range(q_size):
26                node = queue.popleft()
27
28                if node.left:
29                    queue.append(node.left)
30                if node.right:
31                    queue.append(node.right)
32            res += 1
33        
34        return res