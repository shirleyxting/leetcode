# Last updated: 8/16/2026, 9:50:23 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequency for evey number
        # minheap to maintain (freq, num)
        # size: k, to maintain top k largest frequency

        from collections import Counter
        import heapq

        count = Counter(nums) # {num: freq}

        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]