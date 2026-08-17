// Last updated: 8/16/2026, 9:52:40 PM
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

    public boolean isValidBST(TreeNode root) {
        // BST: left is BST, right is BST
        // ALL left < node < ALL right
        
        // each node keeps: val, min, max
        // left.max < node.val < right.min
        return helper(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    // return if root with [minVal from left], [maxVal from right] is a BST
    private boolean helper(TreeNode node, long minVal, long maxVal) {
        if (node == null) return true;
        // System.out.println("node.val = " + node.val + " minVal = " + minVal + " maxVal = " + maxVal);
        if (node.left == null && node.right == null) 
            return node.val > minVal && node.val < maxVal;
        
        return 
            node.val > minVal && node.val < maxVal
            && helper(node.left, minVal, node.val) // left subtree's maxVal should < root
            && helper(node.right, node.val, maxVal); // right subtree's minVal should > root'

    }
}