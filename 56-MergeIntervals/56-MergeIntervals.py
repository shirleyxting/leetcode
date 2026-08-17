# Last updated: 8/16/2026, 9:53:04 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by start point, inv1[l1,r1], inv2[l2,r2]
        # if l2 <= r1, merge -> new_inv[l1, max(r1, r2)]
        if not intervals:
            return
        
        intervals.sort(key=lambda x: x[0])
        # COPY ([:], to avoid modify inputs) first interval into res
        merged = [intervals[0][:]]

        for l, r in intervals[1:]:
            # compare current intv with the last one in merged
            if l <= merged[-1][1]:
                # merge, update the end point
                merged[-1][1] = max(merged[-1][1], r)
            else:
                merged.append([l, r])
        
        return merged
