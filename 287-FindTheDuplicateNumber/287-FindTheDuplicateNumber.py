# Last updated: 8/16/2026, 9:50:37 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # linked list: i -> nums[i]
        # Floyd cycle: entering point of the cycle = duplicate item in arr

        # stage-1: fast, slow pointers to verify the cycle
        # fast永远是slow速度的2倍，且两者相对同一个起点保持"2倍距离"关系
        # start from 0, slow moves 1 step (nums[0]), fast moves 2 steps (nums[nums[0]])
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # stage-2: third pointer starts from index-0, slow stays at meeting point
        # move with same 1 step (same speed)
        # they will meet up at the cycle starting node
        p = 0
        while p != slow:
            p = nums[p]
            slow = nums[slow]
        
        # p 收敛到的位置，它本身就是答案（因为环的入口 = 重复的数字）
        return p

