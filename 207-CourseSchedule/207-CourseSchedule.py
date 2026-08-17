# Last updated: 8/16/2026, 9:51:21 PM
from collections import defaultdict, deque

class Solution:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     # detect DAG, Directed acyclic graph
    #     # DFS

    #     # graph[preq] = [list of courses can be taken after preq]
    #     graph = defaultdict(list)
        
    #     for course, preq in prerequisites:
    #         graph[preq].append(course)
        
    #     # 0: unvisited, 1: visiting, 2: visited
    #     state = [0] * numCourses

    #     # for current course 'c', can we finish the learning of 'c'
    #     def dfs(c: int) -> bool:
    #         # dfs exit
    #         if state[c] == 2: # processed before, no cyle found
    #             return True
    #         if state[c] == 1: # c is in current DFS path, found cycle
    #             return False
            
    #         # mark as visiting and check its neighbors 
    #         state[c] = 1
    #         for c_next in graph[c]:
    #             if not dfs(c_next):
    #                 return False
    #         # mark as visited
    #         state[c] = 2            
    #         return True

    #     for c in range(numCourses):
    #         if not dfs(c):
    #             return False
        
    #     return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BFS
        # process courses without prerequsiites first

        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, preq in prerequisites:
            graph[preq].append(course)
            indegree[course] += 1
        
        # Add all courses with no prerequisites (indegree == 0) to the queue
        queue = deque([c for c in range(numCourses) if indegree[c] == 0])

        finished = 0 # the total number of courses successfully processed
        while queue:
            node = queue.popleft()
            finished += 1
            # decrease the indegree of all downstream neighbor courses
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                # if a neighbor's prerequsites are fully satisfied, add it to the queue
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # if we successfully proceed all courses, no cycle exists
        return finished == numCourses
            


