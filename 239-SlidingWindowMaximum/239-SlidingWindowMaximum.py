# Last updated: 8/16/2026, 9:50:50 PM
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force
        # return [max(nums[i:i+k]) for i in range(len(nums)-k+1)]

        # double-sided queue, dp (save index): elements that can be max-candidate for next window
        # dp[0]: the max of candidates
        # 2 rules to maintain dq:
        #   - every new num, if new >= any candidates, discard those candidates
        #   - if head of dq exceed window size, discard dq[0]

        dq = deque()
        res = []
        n = len(nums)

        for i in range(n):
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            while dq and i - dq[0] >= k:
                dq.popleft()
            
            dq.append(i)
            # for each win, dq[0] is the max canidate index
            # the first win starting at index=k-1
            if i >= k - 1:
                res.append(nums[dq[0]])
        
        return res

