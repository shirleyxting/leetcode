// Last updated: 8/16/2026, 9:51:02 PM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;

        while (root != null) {
            if (p.val > root.val && q.val > root.val) {
                // go to right
                root = root.right;
            } else if (p.val < root.val && q.val < root.val) {
                // go to left
                root = root.left;
            } else {
                return root;
            }
        }
        return null;
    }
}