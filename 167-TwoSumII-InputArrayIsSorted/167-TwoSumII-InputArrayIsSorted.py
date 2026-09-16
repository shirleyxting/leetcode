# Last updated: 9/16/2026, 4:11:30 PM
1class Solution:
2    def twoSum(self, numbers: list[int], target: int) -> list[int]:
3        left, right = 0, len(numbers) - 1
4
5        while left < right:
6            s = numbers[left] + numbers[right]
7            if s == target:
8                return [left + 1, right + 1]
9            elif s < target:
10                left += 1
11            else:
12                right -= 1
13        
14        return None