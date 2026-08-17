// Last updated: 8/16/2026, 9:50:14 PM
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
    int maxDepth = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        // for every node, the 'diameter' which "PASS/CROSS it" = left.depth + right.depth
        // use 'maxDepth' to record current max, cause 'diameter' may not cross root
        if (root == null) return 0;

        getTreeDepth(root);
        return maxDepth;
    }

    private int getTreeDepth(TreeNode root) {
        // calculdate the depth of a treenode root
        // and update maxDepth value
        if (root == null) return 0;
        int maxLeft = getTreeDepth(root.left);
        int maxRight = getTreeDepth(root.right);

        maxDepth = Math.max(maxLeft + maxRight, maxDepth);

        return Math.max(maxLeft, maxRight) + 1;
    }
}