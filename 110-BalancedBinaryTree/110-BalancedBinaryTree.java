// Last updated: 8/16/2026, 9:52:24 PM
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
    // public boolean isBalanced(TreeNode root) {
    //     /**
    //     consider the depth of left, right:
    //     curr.depth = max(left.depth, right.depth) + 1
    //     isBalaced = left.heightBalanced && right.heightBalanced && |left.depth - right.depth|<=1
    //     height balanced: depth of 2 subtrees of every node <= 1

    //     // O(N^2)
    //     */
    //     if(root == null) return true;
    //     if(isBalanced(root.left) == false) return false;
    //     if(isBalanced(root.right) == false) return false;
    //     if(Math.abs(getTreeDepth(root.left) - getTreeDepth(root.right)) > 1) return false;
    //     return true;
    // }

    // private int getTreeDepth(TreeNode curr) {
    //     if(curr == null) return 0;

    //     return Math.max(getTreeDepth(curr.left), getTreeDepth(curr.right)) + 1;
    // }

    // method - 2 imporved DFS, the height fun 
    // return -1 when tree is unbalanced, 
    // and return height if its balanced
    public boolean isBalanced(TreeNode root) {
        if(root == null) return true;

        return getDepth(root) != -1;
    }

    private Integer getDepth(TreeNode curr) {
        if(curr == null) return 0;
        int leftDepth = getDepth(curr.left);
        int rightDepth = getDepth(curr.right);
        if(leftDepth == -1 || rightDepth == -1) return -1;
        if(Math.abs(leftDepth - rightDepth) > 1) return -1;

        return Math.max(leftDepth, rightDepth) + 1;
    }

}