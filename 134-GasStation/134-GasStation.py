# Last updated: 8/20/2026, 6:10:28 PM
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        n = len(gas)
4        diff = [gas[i] - cost[i] for i in range(n)]
5
6        start = 0       # start point
7        curr_tank = 0   # current tank gas amount in current path
8
9        for i in range(n):
10            curr_tank += diff[i]
11            if curr_tank < 0:
12                # reset start point to next point
13                start = i + 1
14                curr_tank = 0
15        
16        # if i can reach to the end of diff, i is the answer
17
18        return start if sum(gas) >= sum(cost) else -1
19
20