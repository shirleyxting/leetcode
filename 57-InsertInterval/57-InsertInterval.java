// Last updated: 8/16/2026, 9:53:01 PM
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        /* 
        1. add all intervals i that i_end < newInterval_start, i++
        2. for overlapping intervals, merge:
            merge_start = min(i_start, newInterval_start)
            merge_end = max(i_end, newInterval_end)
        3. for remianing intervals, add to results
        */
        List<int[]> res = new ArrayList<>();
        int newS = newInterval[0], newE = newInterval[1];
        int n = intervals.length;
        int i = 0;
        while(i < n && intervals[i][1] < newS) {
            res.add(Arrays.copyOf(intervals[i], 2));
            i ++;
        }
        int[] merged = Arrays.copyOf(newInterval, 2);
        while(i < n && intervals[i][0] <= newE) {
            // find ALL overlappings
            merged[0] = Math.min(merged[0], intervals[i][0]);
            merged[1] = Math.max(merged[1], intervals[i][1]);
            i ++;
            System.out.println(merged[0]);
            System.out.println(merged[1]);
        }
        res.add(merged); // add merged interval
        while(i < n) {
            res.add(Arrays.copyOf(intervals[i], 2));
            i ++;
        }
        // convert List<> to int[]
        int[][] res_ = new int[res.size()][2];
        for(int p = 0; p < res.size(); p ++) {
            res_[p][0] = res.get(p)[0];
            res_[p][1] = res.get(p)[1];
        }
        return res_;
    }
}