# Last updated: 8/18/2026, 4:02:23 PM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        # A, B, n-1
4        # A, B, N-1
5        # ...
6        # A, B
7        # time = (max_freq - 1) * (n+1) + max_count
8        #      or len(tasks) is no idle task required
9
10        cnt = Counter(tasks)
11        max_freq = max(cnt.values())    # max freq for tasks
12        max_count = sum(1 for v in cnt.values() if v == max_freq) # count of task_types with max_freq
13
14        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)