# Last updated: 8/16/2026, 9:50:35 PM
class MedianFinder:

    def __init__(self):
        self.small: list[int] = []  # maxHeap(save negatives), save lower half
        self.large: list[int] = []  # minHeap, save larger half
        # size_small - size_large <= 1
        # size_small=size_large -> median = (small[0]+large[0)])/2
        # size_small=size_large+1 -> median = small[0]

    def addNum(self, num: int) -> None:
        # compare small[0], num, large[0]
        if not self.small or -self.small[0] >= num:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        # check size
        if len(self.small) - len(self.large) > 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

        
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        
        return -self.small[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()