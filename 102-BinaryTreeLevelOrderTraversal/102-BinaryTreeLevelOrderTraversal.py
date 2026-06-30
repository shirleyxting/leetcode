# Last updated: 6/29/2026, 11:01:06 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9    #     # BFS
10    #     if not root: return []
11    #     res = []
12    #     queue = deque()
13    #     queue.append(root)
14    #     while queue:
15    #         q_size = len(queue)
16    #         temp = []
17    #         # for i in range(q_size):
18    #         #     curr = queue.popleft()
19    #         #     if curr.left:
20    #         #         temp.append(curr.left.val)
21    #         #         queue.append(curr.left)
22    #         #     if curr.right:
23    #         #         temp.append(curr.right.val)
24    #         #         queue.append(curr.right)
25
26    #         # after poping up from queue, adding the val into "temp"
27    #         # avoid init res and simiply left/right condition
28    #         for i in range(q_size):
29    #             curr = queue.popleft()
30    #             temp.append(curr.val)
31
32    #             if curr.left:
33    #                 queue.append(curr.left)
34    #             if curr.right:
35    #                 queue.append(curr.right)
36                
37    #         # if len(temp) != 0:
38    #         # 因为我们在进入 while queue: 循环前已经处理了 not root 的边界情况，所以只要进入了循环，当前的 queue 里面一定有有效的节点，这意味着 temp 绝对不会为空。因此，这个条件判断是多余的，在 Python 中直接 res.append(temp) 即可。
39    #         # 如果非要判空，利用 Python 的隐式布尔值特性，写成 if temp: 也比 len(temp) != 0 更具 Python 风格（Pythonic）。
40    #         res.append(temp)
41        
42    #     return res
43
44    # clean version
45    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
46        if not root: 
47            return []
48        
49        queue = deque()
50        queue.append(root)
51
52        res = []
53
54        while queue:
55            q_size = len(queue)
56            temp = []
57            for _ in range(q_size): # 用不到变量 i 时，惯例使用下划线 _
58                curr = queue.popleft()
59                temp.append(curr.val) # add val when poping, more clear
60
61                # push nodes in next level into queue
62                if curr.left:
63                    queue.append(curr.left)
64                if curr.right:
65                    queue.append(curr.right)
66
67            # 因为进入循环的前提是有节点，此时 temp 必然不为空，直接 append
68            res.append(temp)
69        
70        return res
71
72
73        