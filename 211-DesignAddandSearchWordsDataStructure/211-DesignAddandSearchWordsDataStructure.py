# Last updated: 8/28/2026, 10:28:39 PM
1# a set of words, repeatedly search, and is not "exact match"
2# if its "prefix matcg", "wildcard", those needs per char comparison -> use Trie, prefix tree
3
4class TrieNode:
5    __slots__ = ('is_end', 'children')
6    
7    def __init__(self):
8        self.is_end = False     # marker for whole word
9        self.children = {}      # char -> TrieNode
10
11class WordDictionary:
12
13    def __init__(self):
14        self.root = TrieNode()  # dummy root node as start point
15
16    def addWord(self, word: str) -> None:
17        node = self.root
18        for c in word:
19            if c not in node.children:
20                node.children[c] = TrieNode()
21            # move to next step
22            node = node.children[c]
23        
24        node.is_end = True
25        
26
27    # for '.', DFS search for all branches
28    def search(self, word: str) -> bool:
29
30        # if word[idx:] exits in node
31        # 从当前的Trie节点node出发，能不能匹配上word从idx往后剩下的部分
32        def dfs(node: TrieNode | None, idx: int) -> bool:
33            # exit
34            if idx == len(word):
35                return node.is_end
36            
37            ch = word[idx]
38            if ch == '.':   # search for all branches
39                for child in node.children.values():    # iterate thru values (TrieNodes)
40                    if dfs(child, idx + 1):
41                        return True     # return immediatly once found
42                return False
43            else:
44                if ch not in node.children:
45                    return False
46                
47                # if ch was found, move forward to check next ch @ idx+1
48                return dfs(node.children[ch], idx + 1)
49
50
51        
52        return dfs(self.root, 0)
53        
54
55
56# Your WordDictionary object will be instantiated and called as such:
57# obj = WordDictionary()
58# obj.addWord(word)
59# param_2 = obj.search(word)