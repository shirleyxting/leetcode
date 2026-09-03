# Last updated: 9/3/2026, 4:37:44 PM
1class MedianFinder:
2    # median only needs 2 numbers, split list into 2 half
3    #   median -> left_max, right_min
4    # left part: max_heap;  right part: min_heap
5
6    # odd length: len(left) - len(right) = 1 -> median = left[0]
7    # even                  =           ->  median = (left[0] + right[0])/2
8    def __init__(self):
9        self.left = []  # max heap: saves -num
10        self.right = [] # min heap: saves num
11
12
13    def addNum(self, num: int) -> None:
14        # compare left[0], num, right[0]
15        # if left is empty or num should be put in left
16        if not self.left or -self.left[0] >= num:
17            heapq.heappush(self.left, -num)
18        else:
19            heapq.heappush(self.right, num)
20        
21        # balance left and right size
22        if len(self.left) - len(self.right) > 1:
23            # if left has more item -> pop from left and push to right
24            heapq.heappush(self.right, -heapq.heappop(self.left))
25        elif len(self.right) > len(self.left):
26            # pop from right, push to left
27            heapq.heappush(self.left, -heapq.heappop(self.right))
28        
29
30    def findMedian(self) -> float:
31        if len(self.left) == len(self.right):
32            return (-self.left[0] + self.right[0]) / 2
33        else:
34            return -self.left[0]
35        
36
37
38# Your MedianFinder object will be instantiated and called as such:
39# obj = MedianFinder()
40# obj.addNum(num)
41# param_2 = obj.findMedian()