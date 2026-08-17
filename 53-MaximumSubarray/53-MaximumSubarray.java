// Last updated: 8/16/2026, 9:53:11 PM
class Solution {
    // public int maxSubArray(int[] nums) {
    //     // brute force - TLE
    //     // step1 - get max sum of subset starting with index-i
    //     // step2- return max(step1 results)
    //     int n = nums.length;
    //     int res = Integer.MIN_VALUE;
    //     for(int i = 0; i < n; i ++) {
    //         int currSum = 0;
    //         for(int j = i; j < n; j ++) {
    //             currSum += nums[j];
    //             res = Math.max(currSum, res);
    //             // res = max sum of subset starting with index-i
    //         }
    //     }
    //     return res;
    // }
    
    // public int maxSubArray(int[] nums) {
    //     // recursive - TLE
    //     if(nums.length == 0) return Integer.MIN_VALUE;
    //     if(nums.length == 1) return nums[0];
    //     System.out.println("Integer.MIN_VALUE + (-7) " + (Integer.MIN_VALUE - 7));
    //     return helper(nums, 0, false);
    // }

    // private int helper(int[] nums, int i, boolean mustPick) {
    //     // return max subset sum in nums[i:],
    //     // mustPick: if the subset MUST starting from nums[i]
    //     // PickFlag=true -> max(nums[i], nums[i] + helper(nums, i+1, true))
    //     //         false -> max(helper(nums, i, true) + helper(nums, i+1, false))

    //     // recursion - exit, 
    //     // if mustPick=True, max(nums[n-1], nums[n-1]+(n,true)), so shoudl return 0 
    //     //             false, max((n-1,true), (n,false)), so return MIN
    //     if(i >= nums.length) {
    //         if(mustPick) return 0;
    //         return Integer.MIN_VALUE;
    //     }
    //     if(mustPick) {
    //         return Math.max(nums[i], nums[i] + helper(nums, i+1, true));
    //     }
    //     return Math.max(helper(nums, i, true), 
    //         helper(nums, i+1, false));
    // }

    // DP-1 top-down, add memo on top of recursion
    // use one example, draw recursion calls to the end -> many re-calculation -> memo -> dp
    // public int maxSubArray(int[] nums) {
    //     int n = nums.length;
    //     if(n == 0) return Integer.MIN_VALUE;

    //     int[][] dp = new int[n+1][2];
    //     // dp[i][0]: maxSum of subset from nums[i:], NOT must pick nums[i]
    //     // dp[i][1]: maxSum of subset from nums[i:], must pick nums[i]
        
    //     // base 'exit' cases
    //     dp[n][0] = Integer.MIN_VALUE;
    //     dp[n][1] = 0;

    //     for(int i = n - 1; i >= 0; i --) {
    //         dp[i][1] = Math.max(nums[i], nums[i] + dp[i+1][1]);
    //         dp[i][0] = Math.max(dp[i][1], dp[i+1][0]);
    //     }
    //     return dp[0][0];
    // }

    // DP-2-Bottom-Up
    // if you feel top-down is hard to get the base case value
    // try 'bottom-up'
    // public int maxSubArray(int[] nums) {
    //     int n = nums.length;
    //     int[][] dp = new int[n][2];
    //     // dp[i][0]: maxSum of subset from nums[:i], NOT must pick nums[i]
    //     // dp[i][1]: maxSum of subset from nums[:i], must pick nums[i]

    //     // base case
    //     dp[0][0] = nums[0]; // get max subset sum for [nums[0]] -> nums[0]
    //     dp[0][1] = nums[0];

    //     for(int i = 1; i < n; i ++) {
    //         dp[i][1] = Math.max(nums[i], nums[i] + dp[i-1][1]);
    //         dp[i][0] = Math.max(dp[i][1], dp[i-1][0]);
    //     }

    //     return dp[n-1][0];
    // }


    // from DP, we found dp[i] only relies on dp[i+1]
    // so no need to keep whole dp[][]
    // just record dp[i+1], and update MaxTillNow
    // public int maxSubArray(int[] nums) {
    //     int currMax = 0, maxTillNow = Integer.MIN_VALUE;
    //     for(int num: nums) {
    //         currMax = Math.max(num, num + currMax);
    //         maxTillNow = Math.max(currMax, maxTillNow);
    //     }
    //     return maxTillNow;
    // }


    // Divide-Conquer
    // subset with max sum will lie:
    // 1. left-half: [L, mid-1]
    // 2. right-half: [mid+1, R]
    // 3. middle: [L`, mid-1] + [mid] + [mid+1, R`], with L`>=L, R`<=R
    // public int maxSubArray(int[] nums) {
    //     return helper(nums, 0, nums.length-1);
    // }

    // // get max subset sum for nums[l:r]
    // private int helper(int[] nums, int l, int r) {
    //     if(l > r) return Integer.MIN_VALUE;

    //     int mid = l + (r-l)/2;
    //     int lSum = 0, rSum = 0;

    //     // lSum: max subset sum in [l`, mid-1], subset ends with mid-1
    //     for(int i = mid-1, currSum = 0; i >= l; i --) {
    //         currSum += nums[i];
    //         lSum = Math.max(lSum, currSum);
    //     }
    //     // rSum: max subset sum in [mid+1, r`], subset starts from mid+1
    //     for(int i = mid+1, currSum = 0; i <= r; i ++) {
    //         currSum += nums[i];
    //         rSum = Math.max(rSum, currSum);
    //     }

    //     return Math.max(
    //         Math.max(
    //         helper(nums, l, mid-1),
    //         helper(nums, mid+1, r)
    //         ),
    //         lSum + nums[mid] + rSum
    //     );
    // }
    

    // Optimized Divide & Conquer
    // pre-calculate the lSum, rSum
    // starts[i] = max subset sum, starts from nums[i]
    // ends[i] =                   ends with

    private int[] starts, ends;
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        // deep copy of nums, 'starts=nums is wrong'
        starts = Arrays.copyOf(nums, n);
        ends = Arrays.copyOf(nums, n);
        System.out.println(Arrays.toString(ends));
        System.out.println(Arrays.toString(starts));
        for(int i = 1; i < n; i ++) ends[i] += Math.max(0, ends[i-1]);
        for(int i = n-2; i >= 0; i --) starts[i] += Math.max(0, starts[i+1]);
        System.out.println(Arrays.toString(ends));
        System.out.println(Arrays.toString(starts));
        return helper(nums, 0, n-1);
    }

    private int helper(int[] nums, int l, int r) {
        if(l == r) return nums[l];
        int mid = l + (r-l) / 2;

        return Math.max(
            Math.max(
                helper(nums, l, mid),
                helper(nums, mid+1, r)
            ), 
            ends[mid] + starts[mid+1]
        );
    }

}