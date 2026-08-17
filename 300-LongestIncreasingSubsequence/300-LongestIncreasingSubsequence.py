# Last updated: 8/16/2026, 9:50:34 PM
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # # brute force
        # n = len(nums)

        # # len of increading subsequence ending at nums[i]
        # def list_end_at(i: int) -> int:
        #     best = 1    # at least nums[i] itself counts
            
        #     # nums[i], only has 2 choices: add to prev sublist or skip
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             best = max(best, 1 + list_end_at(j))
        #     return best
        
        # return max(list_end_at(i) for i in range(n)) if nums else 0


        # # DP, save overlapping calculations of list_end_at(i)
        # # dp[i] = list_end_at(i) = max(dp[j] for j in range(i)) + 1
        # n = len(nums)
        # # dp[i]: length of increasing sublist ending at nums[i]
        # # init at 1, cause nums[i] itself is one of the result
        # dp = [1] * n
        # for i in range(n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], 1 + dp[j])
        
        # return max(dp) if nums else 0
        
        # Binary search
        # tail[i] = the min ending number, for longest increasing subseq (LIS) with len=i+1
        # for num, if num > all tail, LIS can expand 1 by appending num to the end
        #           else: replace num with first >= num (bisect)
        import bisect

        tail: list[int] = []

        for num in nums:
            i = bisect.bisect_left(tail, num)
            if i == len(tail):
                tail.append(num)
            else:
                tail[i] = num
        
        return len(tail)