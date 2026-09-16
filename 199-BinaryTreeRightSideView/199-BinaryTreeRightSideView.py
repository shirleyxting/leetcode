# Last updated: 9/16/2026, 12:13:55 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: TreeNode | None) -> list[int]:
9        # level order BFS, pick the last element
10        if root is None:
11            return []
12
13        q = deque([root])
14        res = []
15        while q:
16            q_size = len(q)
17            for i in range(q_size):
18                node = q.popleft()
19                if i == q_size - 1:
20                    # last item
21                    res.append(node.val)
22                
23                if node.left: q.append(node.left)
24                if node.right: q.append(node.right)
25        
26        return res
27        