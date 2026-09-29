# Last updated: 9/28/2026, 9:24:31 PM
1class Solution:
2    def findMaxLength(self, nums: List[int]) -> int:
3        # consider 0 as -1 -> get maxlen of subarray with sum = 0
4        # subarray [i+1:j], sum = 0 -> prefix[j] = prefix[i], maxlen = j-i
5        # hashmap: prefix -> idx 
6        #   - first prefix sum, -> index
7
8        first = {0: -1}     # init 0 as idx = -1
9        prefix = 0
10        maxlen = 0
11
12        for i, num in enumerate(nums):
13            # take 0 as -1
14            prefix += 1 if num == 1 else -1
15            if prefix in first:
16                maxlen = max(maxlen, i - first[prefix])
17            else:   # only record first occurred prefix
18                first[prefix] = i
19        
20        return maxlen
21
22
23