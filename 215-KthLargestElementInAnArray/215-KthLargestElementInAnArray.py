# Last updated: 8/16/2026, 9:51:12 PM
class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # minheap to keep the top k largest
    #     # top of the minheap = kth largest

    #     import heapq

    #     heap = []

    #     for num in nums:
    #         heapq.heappush(heap, num)

    #         if len(heap) > k:
    #             heapq.heappop(heap)
        
    #     return heap[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        
        return heap[0]


