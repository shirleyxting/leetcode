// Last updated: 8/16/2026, 9:53:51 PM
class Solution {
    public int maxArea(int[] height) {
                /* 1-Brute Force
        for each 'h', iterate all next heights, and update maxArea

        2 - two pointers.
        l 
        r
        area = min * (r - l)
        GREEDY: only move l/r that points to lower line
        eg: (2,3,6,5,4,1)
        move '1' to '4', will give u possible larger area
        if u move '2' to '3', only results in smaller area
        */

        int res = 0;
        int len = height.length;
        int l = 0, r = len - 1;
        while(l < r) {
            if(height[l] < height[r]) {
                res = Math.max(res, height[l] * (r - l));
                l ++;
            } else {
                res = Math.max(res, height[r] * (r - l));
                r --;
            }
        }
        return res;
    }
}