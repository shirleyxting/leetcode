# Last updated: 8/31/2026, 8:38:49 PM
1class Solution:
2    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
3        # 1 char change every step + shortest path
4        # BFS in undirected graph
5        # node: word, edge: word --- 1 char changed word
6        #  how to find 1 char changed word -> do not compare two words O(n * L), modify 1 char in word O(26*L)
7        
8        word_set = set(wordList)
9        if endWord not in word_set:
10            return 0
11        
12        q = deque([beginWord])
13        visited = {beginWord}
14        steps = 1   # beginWord counts for 1 step
15
16        while q:
17            # BFS level traversal
18            q_size = len(q)
19            for _ in range(q_size):
20                word = q.popleft()
21
22                if word == endWord:
23                    return steps
24
25                # iterate word's neighbors (with 1 char diff)
26                for i in range(len(word)):  # modify word[i] to a diff char
27                    for c in string.ascii_lowercase:
28                        if c == word[i]:    # new char is the same 
29                            continue
30                        
31                        nxt = word[:i] + c + word[i + 1:]
32                        if nxt in word_set and nxt not in visited:
33                            q.append(nxt)
34                            visited.add(nxt)    # mark as visited during enqueue
35            
36            steps += 1
37        
38        return 0
39