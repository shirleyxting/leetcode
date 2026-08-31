# Last updated: 8/30/2026, 9:52:41 PM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        # topo sort
4        graph = defaultdict(list)   # node -> [downstream nodes list]
5        indegree = [0] * numCourses
6
7        for a, b in prerequisites:  # edge: b -> a
8            graph[b].append(a)
9            indegree[a] += 1
10
11        queue = deque([c for c in range(numCourses) if indegree[c] == 0])
12        res = []
13
14        while queue:
15            node = queue.popleft()
16            res.append(node)
17
18            for nxt in graph[node]:
19                indegree[nxt] -= 1
20                if indegree[nxt] == 0:
21                    queue.append(nxt)
22        
23        return res if len(res) == numCourses else []