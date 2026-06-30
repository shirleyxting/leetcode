# Last updated: 6/29/2026, 10:41:20 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        # BFS
10        if not root: return []
11        res = [[root.val]]
12        queue = deque()
13        queue.append(root)
14        while queue:
15            curr_len = len(queue)
16            level = []
17            for i in range(curr_len):
18                curr = queue.popleft()
19                if curr.left:
20                    level.append(curr.left.val)
21                    queue.append(curr.left)
22                if curr.right:
23                    level.append(curr.right.val)
24                    queue.append(curr.right)
25            if len(level) != 0:
26                res.append(level)
27        
28        return res
29
30        