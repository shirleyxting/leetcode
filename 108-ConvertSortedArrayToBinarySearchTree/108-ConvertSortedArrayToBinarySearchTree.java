// Last updated: 8/16/2026, 9:52:22 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // public TreeNode sortedArrayToBST(int[] nums) {
        // in-order = nums
        // 1,2,3,4 -> root = 3
        // 1,2,3,4,5 -> root = 3
        // height-balanced, diff(left.depth, right.depth) <= 1
        // pick middle num as root node

        // int n = nums.length;
        // if(n == 0) return null;
        // if(n == 1) return new TreeNode(nums[0]);

        // TreeNode root = new TreeNode(nums[n/2]);
        // if(n == 2) {
        //     root.left = new TreeNode(nums[0]);
        //     return root;
        // }

        // // java Arrays.copyOfRange(nums, fromIdx, toIdx)
        // // = nums[fromIdx : toIdx - 1]
        // root.left = sortedArrayToBST(Arrays.copyOfRange(nums, 0, n/2));
        // root.right = sortedArrayToBST(Arrays.copyOfRange(nums, n/2+1, n));

        // return root;
    // }


    // method 2 - without slicing the array, 
    // since the copyOfRange takes O(s), s is the size of slice
    // the above is actully o(nlogn) time, space o(n)
    // if we pass the startIdx, endIdx, it could be time O(n), space O(logn)
    /*
    So on first call you make = N/2 + N/2 = N size list
on second call you make = N/4 + N/4 + N/4 + N/4 = N size list
and so on till log N height.

So you'll be taking NLogN time and not N time. If you want to use linear time, use a helper method that just takes the left and right pointer.
    */
    public TreeNode sortedArrayToBST(int[] nums) {
        if(nums.length == 0) return null;
        return buildBST(nums, 0, nums.length - 1);
    }

    private TreeNode buildBST(int[] nums, int start, int end) {
        if(start > end) return null;
        if(start == end) return new TreeNode(nums[start]);

        int mid = start + (end - start) / 2; // avoid overflow
        TreeNode root = new TreeNode(nums[mid]);
        root.left = buildBST(nums, start, mid - 1);
        root.right = buildBST(nums, mid + 1, end);

        return root;
    }

   
}