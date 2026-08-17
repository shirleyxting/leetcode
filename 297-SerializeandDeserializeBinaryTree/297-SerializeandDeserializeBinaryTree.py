# Last updated: 8/17/2026, 4:18:39 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Codec:
9
10    def serialize(self, root):
11        """Encodes a tree to a single string.
12        
13        :type root: TreeNode
14        :rtype: str
15        """
16        # use preorder: root-left-right, to traverse a tree
17        nodes = [] # use null to identify None node
18
19        def preorder(node):
20            if not node:
21                nodes.append("null")
22                return
23            
24            nodes.append(str(node.val))  # convert int to str, ensure list[str]
25            preorder(node.left)
26            preorder(node.right)
27
28        preorder(root)
29        # deserialize input is string
30        # combine list to str with "," as delimiter
31        return ",".join(nodes)
32
33
34    def deserialize(self, data):
35        """Decodes your encoded data to tree.
36        
37        :type data: str
38        :rtype: TreeNode
39        """
40        vals = iter(data.split(","))
41
42        def build():
43            val = next(vals)
44            if val == "null":
45                return None
46            
47            node = TreeNode(int(val))
48            node.left = build() # build left child
49            node.right = build()
50            return node
51
52        return build()
53        
54
55# Your Codec object will be instantiated and called as such:
56# ser = Codec()
57# deser = Codec()
58# ans = deser.deserialize(ser.serialize(root))