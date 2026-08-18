# Last updated: 8/18/2026, 4:14:01 PM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        # # A, B, n-1
4        # # A, B, N-1
5        # # ...
6        # # A, B
7        # # time = (max_freq - 1) * (n+1) + max_count
8        # #      or len(tasks) is no idle task required
9
10        # cnt = Counter(tasks)
11        # max_freq = max(cnt.values())    # max freq for tasks
12        # max_count = sum(1 for v in cnt.values() if v == max_freq) # count of task_types with max_freq
13
14        # return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
15
16        # Greedy
17        # always pick task with max remaining cnt
18        # maxHeap: [cnt]
19        # deque: (cool_end_time, cnt)
20
21        freq = Counter(tasks)
22        heap = [-v for v in freq.values()]
23        heapq.heapify(heap)
24
25        cooldown = deque()      # (cooldown_end_time, cnt)
26
27        time = 0
28        remaining = len(tasks)  # remaining tasks
29
30        while remaining > 0:
31            time += 1
32            if heap:
33                cnt = -heapq.heappop(heap) # get the task with max cnt
34                remaining -= 1
35                cnt -= 1
36                if cnt > 0:
37                    cooldown.append((time + n, cnt))
38            
39            while cooldown and time == cooldown[0][0]:
40                _, c = cooldown.popleft()
41                heapq.heappush(heap, -c)
42        
43        return time