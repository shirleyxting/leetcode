# Last updated: 8/20/2026, 9:50:17 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        # take preorder first node as root.
10        # find root's idx in inoder -> left_tree=inorder[:mid], right_tree=inorder[mid+1:]
11
12        # val -> inorder idx
13        idx_map = {val: i for i, val in enumerate(inorder)}
14
15        self.pre_idx = 0    # current preorder idx (take as root)
16
17        # return root with inorder[left:right]
18        def build(left: int, right: int) -> Optional[TreeNode]:
19            # recursion exit
20            if left > right:
21                return None
22            
23            root_val = preorder[self.pre_idx]
24            self.pre_idx += 1   # handle next "root"
25
26            mid = idx_map[root_val]
27            
28            root = TreeNode(root_val)
29            root.left = build(left, mid - 1)
30            root.right = build(mid + 1, right)
31
32            return root
33        
34        return build(0, len(preorder) - 1)
35