# Last updated: 9/27/2026, 3:26:44 PM
1class Solution:
2    def majorityElement(self, nums: list[int]) -> int:
3        # sort then pick median -> nlogn, o(1)
4        # counter -> o(n), o(n)
5        # boyer-moore
6        # 把 count 理解成「候选相对其他所有元素的净盈余」，不是简单的加减游戏。
7        # 设多数元素是 M，出现次数 > n/2。
8        # 想象你在做「配对抵消」：每遇到一个 M，如果手里有一个「非 M」的余额，就抵消掉一对；
9        # 抵消不了就攒着。因为 M 的数量比其余所有元素加起来还多，不可能被完全抵消——最后手里剩下的候选，一定是 M。
10
11        candidate, count = None, 0
12        for num in nums:
13            if candidate == num:
14                count += 1
15            elif count == 0:
16                candidate = num
17                count = 1
18            else:
19                count -= 1
20        
21        return candidate