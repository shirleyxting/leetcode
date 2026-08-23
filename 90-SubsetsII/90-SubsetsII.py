# Last updated: 8/23/2026, 12:58:05 PM
1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        # sort nums, and pick next DIFF num (skip same values)
4        # backtrack
5
6        nums.sort()
7        res = []
8        path = []   # curr path
9
10        # find legit subset in nums[start:]
11        def backtrack(start: int):
12            res.append(path[:]) # copy path as path is changing
13
14            for i in range(start, len(nums)):
15                # i > start not i > 0
16                # as i==start is the first choice, it should always be selected, otherwise you will skip legit combinations
17                # 去重核心：i > start（不是 i > 0）——只禁止"同一层for循环里横向选到相同数字"
18                # 只有i > start时，才是"在同一层里，前一个兄弟分支已经试过某个值了，现在轮到试下一个候选值"，这时才需要跟"同一层的上一个候选值"比较去重。
19                # 允许"同一条路径纵向连续选相同数字"（比如[2,2]这个子集本身是合法的，必须能生成）
20                if i > start and nums[i] == nums[i-1]:
21                    continue
22                
23                path.append(nums[i])    # select
24                backtrack(i + 1)        # check next element
25                path.pop()              # cancel selection
26        
27        backtrack(0)
28        return res
29
30