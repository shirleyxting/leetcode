# Last updated: 8/16/2026, 9:47:33 PM
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # graph: preq -> [next1, next2, ..]
        # indegree: task_id -> indegree
        # preqs: task -> [prev1, prev2, ..]
        # finish: task_id -> the earliest finished time for task_id
        #   finish[task] = runtime[task] + max(finish[prev1], finish[prev2], ..)

        graph = defaultdict(list)
        indegree = defaultdict(int)
        finish = defaultdict(int)
        preqs = defaultdict(list)

        for preq, course in relations:
            graph[preq].append(course)
            indegree[course] += 1
            preqs[course].append(preq)

        q = deque()
        # check indegree=0 nodes
        for i in range(1, n + 1):
            if indegree[i] == 0:
                finish[i] = time[i - 1]
                q.append(i)
        
        while q:
            node = q.popleft()
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
                    finish[nxt] = time[nxt - 1] + max(finish[p] for p in preqs[nxt])

        return max(finish.values())
