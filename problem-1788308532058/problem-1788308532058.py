# Last updated: 9/1/2026, 5:22:12 PM
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        # greedy
4        jumps = 0
5
6        curr_end = 0    # current layer right boundary
7        farthest = 0    # the farthest can reach in next jump
8        # once visit all nodes in currn layer, farthest = next layer right boundary
9
10        for i in range(len(nums) - 1):
11            # 停在 n-2 就够
12            # 题目保证一定能到终点，所以「把 cur_end 推到 >= n-1 的那一跳」一定发生在某个 i <= n-2 上，那时 jumps 已经 +1 了。
13            # 终点所在的层不需要再跳出去，循环提前一格结束，正好只数「进入终点层」这一跳，不数「跳出终点层」这个假动作。
14            farthest = max(farthest, i + nums[i])
15
16            if i == curr_end:
17                # reach the curr layer right boundary, need jump to next layer
18                # now, farthest = next layer's right boundary
19                jumps += 1
20                curr_end = farthest
21        
22        return jumps