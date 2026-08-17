// Last updated: 8/16/2026, 9:50:52 PM
class Solution {
    // public int[] productExceptSelf(int[] nums) {
    //     int n = nums.length;
    //     int[] res = new int[n];
    //     /* 
    //     result:[bcd,    acd,    abd,    abc]
    //     prefix:[1,      a,      ab,     abc]
    //     suffix:[bcd,    cd,     d,      1]
        
    //     res[i] = pre[i]*suff[i]
    //     pre[i]: product of all element before i
    //     suff[i]                        after
    //     */
    //     int[] pre = new int[n];
    //     int[] suff = new int[n];
    //     pre[0] = 1;
    //     suff[n - 1] = 1;
    //     for(int i = 1; i < n; i ++) {
    //         pre[i] = pre[i - 1] * nums[i - 1];
    //     }
    //     for(int i = n - 2; i >= 0; i --) {
    //         suff[i] = suff[i + 1] * nums[i + 1];
    //     }

    //     for(int i = 0; i < n; i ++) {
    //         res[i] = pre[i] * suff[i];
    //     }

    //     return res;
    // }

    public int[] productExceptSelf(int[] nums) {
        // res saves pre, and then iterate thru suff, update res value
        // Space: O(1), directly save prefix, suffix to final results
        int n = nums.length;
        int[] res = new int[n];
        // res[0] = 1;
        // for(int i = 1; i < n; i++) {
        //     res[i] = res[i-1]*nums[i-1];
        // }
        Arrays.fill(res, 1);
        int curr = 1;
        for(int i = 0; i < n; i++) {
            res[i] *= curr;
            curr *= nums[i];
        }
        curr = 1;
        for(int i = n - 1; i >= 0; i--) {
            res[i] *= curr;
            curr *= nums[i];
        }
        return res;
    }
}