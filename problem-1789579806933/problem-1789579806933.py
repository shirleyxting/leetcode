# Last updated: 9/16/2026, 10:30:06 AM
1class Solution:
2    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
3        # # diff array when size is small, like here is 1000
4        # diff = [0] * 1001 # needs diff[1000]
5
6        # for num, start, end in trips:
7        #     diff[start] += num
8        #     diff[end] -= num
9        
10        # # prefix sum at i = how many people are in the car at time-i
11        # onboard = 0 # prefix sum, running sum
12        # for i in range(1001):
13        #     onboard += diff[i]
14        #     if onboard > capacity:
15        #         return False
16        # return True
17
18        # sorted events, drop_off should be placed at fronmt of pick_up
19        events = []     # (ts, num_change_delta)
20        for num, start, end in trips:
21            events.append((start, num))
22            events.append((end, -num))
23        
24        events.sort()   # first off then on
25
26        onboard = 0 # running sum, current cnt in the car
27        for _, delta in events:
28            onboard += delta
29            if onboard > capacity:
30                return False
31        
32        return True