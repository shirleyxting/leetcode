// Last updated: 8/16/2026, 9:51:17 PM
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        //sliding window
        int res = Integer.MAX_VALUE;
        int l = 0;
        int subsum = 0;

        for(int r = 0; r < nums.length; r ++) {
            // add r into window
            subsum += nums[r];
            if (subsum >= target) {
                // remove leftmost num until condition NOT satisfy
                while(subsum >= target) {
                    // before adjust the window, updating res
                    res = Math.min(res, r - l + 1);
                    // shrink the window
                    subsum -= nums[l];
                    l ++;
                }
            }
        }

        if (res == Integer.MAX_VALUE) return 0;
        return res;
    }
}