# Last updated: 8/28/2026, 9:09:31 PM
1# Trie is built on TrieNode
2
3class TrieNode:
4    __slots__ = ('is_end', 'children')  # avoid attribute typos
5
6    def __init__(self):
7        self.is_end = False     # marker: if word ends at curr node
8        self.children = {}      # char -> Trie() node
9
10class Trie:
11
12    def __init__(self):
13        self.root = TrieNode()  # root does not present any char, just dummy node as start point
14
15    def insert(self, word: str) -> None:
16        node = self.root
17        for c in word:
18            if c not in node.children:
19                node.children[c] = TrieNode()
20            node = node.children[c]
21
22        # reach the end node, mark it
23        node.is_end = True
24    
25    # find chars of s in Trie, if char not found return None, if finish search, return the end TrieNode
26    def _find(self, s: str):
27        node = self.root
28        for c in s:
29            if c not in node.children:
30                return None
31            node = node.children[c]
32        
33        return node
34
35
36    def search(self, word: str) -> bool:
37        node = self._find(word)
38        return (node is not None) and (node.is_end)
39        
40
41    def startsWith(self, prefix: str) -> bool:
42        return self._find(prefix) is not None
43
44
45# Your Trie object will be instantiated and called as such:
46# obj = Trie()
47# obj.insert(word)
48# param_2 = obj.search(word)
49# param_3 = obj.startsWith(prefix)