# Last updated: 9/17/2026, 4:04:42 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        # # brute force: O(n * max(piles))
4        # # k: [1, max(pile)]
5        # for k in range(1, max(piles) + 1, 1):
6        #     hours_needed = sum(math.ceil(pile / k) for pile in piles)
7        #     if hours_needed <= h:
8        #         return k
9        # return -1
10
11        # binary search k, O(n*log(max_piles))
12        # binary search on the answer
13        # ans is a number we need to guess, and T/F is decided by feasible(), 
14        # while feasible() is monotonic, so for the ans guess range, we will get: F F T T T T 
15        # and we need to find the leftmost T -> binary search
16
17        # ① 题目给定的数：h = 8 小时                       ← 硬约束，不能动
18        # ② 要求的答案：吃的速度 k                          ← 未知，越小越好
19        #    范围 [1, max(piles)] = [1, 11]
20        #    下界 1：最慢的速度，一定能吃完（只是慢）
21        #    上界 11：一小时一堆，再快没意义（一小时最多吃一堆）
22        # ③ feasible(k)：把速度卡死成 k，算 h 这种资源最少要多少：
23        #    最少小时数 H = Σ ceil(pile / k)              ← 每堆单独算，不够一份也占一小时
24        # ④ 返回：H <= h
25        #    单调性：k 越大 → H 越小 → 越容易 <= h → F F F T T T，找第一个 T
26
27        def feasible(k: int) -> bool:
28            # get the hours needed to finished all piles
29            H = sum(math.ceil(pile / k) for pile in piles)
30            # if H<=h, then koko can do it with k speed
31            # else               NO
32            return H <= h
33        
34        # iterate thru all possible k: [1, max(piles)]
35        # feasible will give answer: F F T T T, we need the first T
36        left, right = 1, max(piles)
37        res = 0
38        while left <= right:
39            mid = (left + right) // 2
40            if feasible(mid):
41                # move left to find any possible smaller answer
42                res = mid
43                right = mid - 1
44            else:
45                # move right
46                left = mid + 1
47        
48        return res
49                
50                
51