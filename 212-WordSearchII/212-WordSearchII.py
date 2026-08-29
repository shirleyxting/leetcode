# Last updated: 8/29/2026, 4:14:46 PM
1class TrieNode:
2    __slots__ = ('word', 'children')
3
4    def __init__(self):
5        # when reaching to word end, set word = 'word'
6        self.word = None
7        self.children = {}  # char -> TrieNode
8
9
10class Solution:
11    # dfs to iterate Trie
12    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
13        m, n = len(board), len(board[0])
14        res = []
15
16        # build Trie/prefix tree
17        root = TrieNode()   # dummy start point
18        for word in words:
19            node = root     # each work starts from root
20            for c in word:
21                if c not in node.children:
22                    node.children[c] = TrieNode()
23                node = node.children[c]
24            
25            node.word = word    # reach end of the word
26
27
28        # node: the curr path
29        # board[r][c]: next ch to check
30        # start from board[r][c], if it can extend node path to find whole word
31        def dfs(r: int, c: int, node: TrieNode) -> None:
32            ch = board[r][c]
33            if ch not in node.children:
34                # exit early
35                return
36            
37            child = node.children[ch]
38
39            # if child TrieNode has reached the end of word
40            # append to res
41            if child.word is not None:
42                res.append(child.word)
43                child.word = None   # mark as visited, to avoid duplicate results (causing by diff dfs paths)
44            
45            # select current ch: board[r][c]
46            board[r][c] = '#'       # to avoid curr path to revisit
47
48            # iterate 4 dirs of possible chars, starting from child node
49            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
50                nr, nc = r + dr, c + dc
51
52                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
53                    dfs(nr, nc, child)
54            
55            # revoke selection
56            board[r][c] = ch
57
58
59        
60
61        for i in range(m):
62            for j in range(n):
63                # iterate all possible start char, matching with root node
64                dfs(i, j, root) 
65        
66        return res
67
68