# Last updated: 9/15/2026, 5:15:02 PM
1class RecentCounter:
2
3    def __init__(self):
4        # q: curr active window queue
5        self.q = deque()
6        self.win_size = 3000
7
8    def ping(self, t: int) -> int:
9        self.q.append(t)
10
11        while self.q[0] < t - self.win_size:
12            self.q.popleft()
13        
14        return len(self.q)
15
16        
17
18
19# Your RecentCounter object will be instantiated and called as such:
20# obj = RecentCounter()
21# param_1 = obj.ping(t)