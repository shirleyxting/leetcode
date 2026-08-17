# Last updated: 8/16/2026, 9:49:12 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # # brute force: O(n * max(piles))
        # # k: [1, max(pile)]
        # for k in range(1, max(piles) + 1, 1):
        #     hours_needed = sum(math.ceil(pile / k) for pile in piles)
        #     if hours_needed <= h:
        #         return k
        # return -1

        # binbary search k, O(n*log(max_piles))

        def hours_needed(k: int) -> int:
            return sum(math.ceil(pile / k) for pile in piles)
        
        left, right = 1, max(piles)
        res = -1

        while left <= right:
            mid = (left + right) // 2
            hours = hours_needed(mid)
            if hours <= h: # condition met, search left to find lower k
                res = mid
                right = mid - 1
            else:   # condition not net, find larger k
                left = mid + 1

        return res
                
