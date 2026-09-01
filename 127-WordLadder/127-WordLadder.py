# Last updated: 8/31/2026, 8:44:02 PM
1class Solution:
2    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
3        # 1 char change every step + shortest path
4        # BFS in undirected graph
5        # node: word, edge: word --- 1 char changed word
6        #  how to find 1 char changed word -> do not compare two words O(n * L), modify 1 char in word O(26*L)
7
8        # so no need to actually build the graph, just need get each node's nerighbors
9        # -> beginWord at Layer-1, endWord at Layer-N, return N
10        # -> so its level order BFS
11        
12        word_set = set(wordList)
13        if endWord not in word_set:
14            return 0
15        
16        q = deque([beginWord])
17        visited = {beginWord}
18        steps = 1   # beginWord counts for 1 step
19
20        while q:
21            # BFS level traversal
22            q_size = len(q)
23            for _ in range(q_size):
24                word = q.popleft()
25
26                if word == endWord:
27                    return steps
28
29                # iterate word's neighbors (with 1 char diff)
30                for i in range(len(word)):  # modify word[i] to a diff char
31                    for c in string.ascii_lowercase:
32                        if c == word[i]:    # new char is the same 
33                            continue
34                        
35                        nxt = word[:i] + c + word[i + 1:]
36                        if nxt in word_set and nxt not in visited:
37                            q.append(nxt)
38                            visited.add(nxt)    # mark as visited during enqueue
39            
40            steps += 1
41        
42        return 0
43