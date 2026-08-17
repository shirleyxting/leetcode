# Last updated: 8/16/2026, 9:50:08 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # # brute force
        # n = len(nums)
        # res = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         if sum(nums[i: j+1])== k:
        #             res += 1
        # return res

        # # brute-force: version2
        # # sum[nums[i:j+1]] = curr_sum + nums[j]
        # n = len(nums)
        # count = 0

        # for i in range(n):
        #     curr_sum = 0
        #     for j in range(i, n):
        #         curr_sum += nums[j]
        #         if curr_sum == k:
        #             count += 1
        # return count


        # sum[i:j] = prefix_sum[j] - prefix_sum[i]
        # sum[i:j] == k -> prefix_sum[i] = prefix_sum[j] - k
        # prefix_count: prefix -> prefix occurence count
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        n = len(nums)
        res = 0
        running_sum = 0

        for num in nums:
            running_sum += num
            res += prefix_count[running_sum - k] 
            prefix_count[running_sum] += 1
        
        return res