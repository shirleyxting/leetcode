# Last updated: 9/28/2026, 8:46:36 PM
1class Solution:
2    def sortColors(self, nums: list[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        # counter = Counter(nums)
7        
8        # for i in range(counter[0]):
9        #     nums[i] = 0
10        # for i in range(counter[0], counter[0] + counter[1]):
11        #     nums[i] = 1
12        # for i in range(counter[0] + counter[1], len(nums)):
13        #     nums[i] = 2
14
15        # in-place partition
16        # [0, low) = 0, [low, mid) = 1, [mid, high] = ?, (high, n-1] = 2
17
18        n = len(nums)
19        low, mid, high = 0, 0, n - 1
20
21        while mid <= high:
22            if nums[mid] == 0:
23                # switch mid, low, and low comes from [low, mid) = 1
24                # so both low and mid can move one step
25                nums[mid], nums[low] = nums[low], nums[mid]
26                mid += 1
27                low += 1
28            elif nums[mid] == 1:
29                mid += 1
30            else:   # switch mid, high, high is from [mid, high], unprocessed area
31                # so after switch, we cannot move mid
32                nums[mid], nums[high] = nums[high], nums[mid]
33                high -= 1
34        
35
36        
37        