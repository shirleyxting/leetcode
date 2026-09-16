# Last updated: 9/16/2026, 10:26:35 AM
1class Solution:
2    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
3        # diff array when size is small, like here is 1000
4        diff = [0] * 1001 # needs diff[1000]
5
6        for num, start, end in trips:
7            diff[start] += num
8            diff[end] -= num
9        
10        # prefix sum at i = how many people are in the car at time-i
11        onboard = 0 # prefix sum, running sum
12        for i in range(1001):
13            onboard += diff[i]
14            if onboard > capacity:
15                return False
16        return True