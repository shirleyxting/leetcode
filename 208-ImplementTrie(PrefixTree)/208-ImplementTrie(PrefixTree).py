# Last updated: 8/28/2026, 9:03:42 PM
1# Trie is built on TrieNode
2
3class TrieNode:
4    def __init__(self):
5        self.is_end = False     # marker: if word ends at curr node
6        self.children = {}      # char -> Trie() node
7
8class Trie:
9
10    def __init__(self):
11        self.root = TrieNode()  # root does not present any char, just dummy node as start point
12
13    def insert(self, word: str) -> None:
14        node = self.root
15        for c in word:
16            if c not in node.children:
17                node.children[c] = TrieNode()
18            node = node.children[c]
19
20        # reach the end node, mark it
21        node.is_end = True
22    
23    # find chars of s in Trie, if char not found return None, if finish search, return the end TrieNode
24    def _find(self, s: str):
25        node = self.root
26        for c in s:
27            if c not in node.children:
28                return None
29            node = node.children[c]
30        
31        return node
32
33
34    def search(self, word: str) -> bool:
35        node = self._find(word)
36        return (node is not None) and (node.is_end)
37        
38
39    def startsWith(self, prefix: str) -> bool:
40        return self._find(prefix) is not None
41
42
43# Your Trie object will be instantiated and called as such:
44# obj = Trie()
45# obj.insert(word)
46# param_2 = obj.search(word)
47# param_3 = obj.startsWith(prefix)