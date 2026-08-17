// Last updated: 8/16/2026, 9:50:16 PM
// 0/1 knapsack problem, keep it or not with weight W
// method 1 - brute force
// for each element, we have 2 choices, to add or not in subset
// time: O(2^N), N = nums.length
// class Solution {
//     public boolean answer;
//     public boolean canPartition(int[] nums) {
//         // subset sum = total_sum / 2
//         int sum = 0;
//         for(int n: nums) sum += n;
//         if (sum % 2 == 1) return false; // target cannot be odd
//         int target = sum / 2;

//         // brute force: for each 'n', choose it or not -> O(2^n)
//         answer = false;
//         helper(0, nums, target);
//         return answer;
//     }

//     private void helper(int i, int[] nums, int target) {
//         if (i >= nums.length) return; // recursion exit
//         if (target == 0) answer = true;
//         // choose nums[i] or not
//         helper(i+1, nums, target - nums[i]); // choose nums[i]
//         helper(i+1, nums, target); // NOT choose nums[i]
//     }
// }

// method 2 - MEMO + TOP-DOWN recursion
// hwo to reduce/remove duplicate cases in method-1 brute force?
// save results for boolean[index i, remaining target]
// time, space = O(N * sum), N = nums.length, sum = sum of nums[]

/** boolean[][] memo will results in Time Limit Error
cause the deafult 'false' value could be:
- not explored/visited yet
- cannot find a desried subset with target sum
==> initialize with NULL (Boolean[][], object Boolean array)
    or use int[][], 0 means not visited, 1 means TRUE, 2 mease FALSE
*/
// class Solution {
//     Boolean[][] memo;
//     public boolean canPartition(int[] nums) {
//         int sum = 0;
//         for(int n: nums) sum += n;
//         if (sum % 2 == 1) return false;
//         int target = sum / 2;

//         memo = new Boolean[target+1][nums.length];

//         return helper(0, nums, target);
//     }

//     private boolean helper(int i, int[] nums, int target) {
//         if (i >= nums.length || target < 0) return false; //recursion exit
//         // if visited before, directly return the calculated value
//         if (memo[target][i] != null) return memo[target][i];
//         if (target == 0) return true;

//         // choose nums[i] or not
//         memo[target][i] = helper(i+1, nums, target - nums[i]) 
//             || helper(i+1, nums, target);

//         return memo[target][i];
//     }
// }


// method 3 - DP
/**
dp[i][j] = dp[i - nums[j-1]][j-1] OR dp[i][j-1] (choose nums[j-1] or not)
 */
// class Solution {
//     public boolean canPartition(int[] nums) {
//         int sum = 0, len = nums.length;
//         for(int n: nums) sum += n;
//         if(sum % 2 == 1) return false;
//         int target = sum / 2;

//         Boolean[][] dp = new Boolean[sum+1][len+1];
//         // whether a subset(nums[:j], [0,1,...,j-1] first j elements) can make sum 'i'
//         for(int i = 0; i <= sum; i ++) {
//             for (int j = 0; j <= len; j ++) {
//                 if (i == 0 || j == 0) dp[i][j] = false;
//                 else if (nums[j-1] == i) dp[i][j] = true; // found target
//                 // if current nums[j] > sum 'i', then skip and take previous value
//                 else if (nums[j-1] > i) dp[i][j] = dp[i][j-1];
//                 // choose nums[j-1] or not
//                 else dp[i][j] = dp[i - nums[j-1]][j-1] || dp[i][j-1];
//             }
//         }
//         return dp[target][len];
//     }
// }


// method 4 - DP - one dimensional
// https://www.youtube.com/watch?v=z_VLFGzQQtk
class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0, len = nums.length;
        for(int n: nums) sum += n;
        if(sum % 2 == 1) return false;
        int target = sum / 2;

        boolean[] dp = new boolean[sum + 1];
        dp[0] = true;

        for(int n: nums) {
            for(int t = target; t > 0; t --) {
                if(t >= n) dp[t] = dp[t] || dp[t-n]; // choose 'n' or not
            }
        }
        return dp[target];
    }
}



// method 3 - Dynamic Programming, bottom-up
// for nums[i], if we already known all possible sums that the remaining elements can make
// if nums[i] + any sum = target or any sum = target, then TRUE
// Bottom-Up: get all possible sum from the last element

// class Solution {
//     public boolean canPartition(int[] nums) {
//         int sum = 0;
//         for(int n: nums) sum += n;
//         if(sum % 2 == 1) return false;
//         int target = sum / 2;

//         // use HashSet to avoid duplicate sum
//         Set<Integer> dp = new HashSet<>();
//         dp.add(0);

//         for(int i = nums.length - 1; i >= 0; i --) {
//             // we cannot update dp and iterate dp at the same time
//             // modify 'temp' while iterating 'dp', to avoid ConcurrentModificationException
//             Set<Integer> temp = new HashSet<>();
//             for(int t: dp) {
//                 int newSum = nums[i] + t;
//                 if (newSum == target) return true;
//                 temp.add(newSum);
//                 temp.add(t);
//             }
//             // add all new 'sums' to 'dp', after eahc iteration
//             // otherwise, dp will always only have '0' inside
//             dp = temp;
//         }
        
//         return dp.contains(target);
//     }
// }
