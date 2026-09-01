# Last updated: 9/1/2026, 4:28:39 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        # greedy
4        farthest = 0    # the farthest idx we can reach so far
5
6        for i, num in enumerate(nums):
7            if farthest < i:
8                # if cannot reach current idx, exit
9                return False
10            else:
11# nums[i] 是站在下标 i 时的跳跃力，它把你从下标 i 弹出去，所以落点最远是 i + nums[i]。
12# farthest 是从某个更早的下标攒出来的可达距离，跟「下标 i 的跳跃力」没关系，两者不能相加
13# farthest + nums[i] 等于假设你「先白嫖 farthest 那么远，再从那里用 i 的油跳一次」，多算了一段你没有油的距离。
14                farthest = max(farthest, i + nums[i])
15
16                if farthest >= len(nums) - 1:
17                    return True
18
19        return True