// Last updated: 8/16/2026, 9:50:54 PM
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
        // case-1: p, q on the left/right side, root = LCA
        // case-2: LCA = p, q is the children of p
        // case-3: LCA = q, p is the children of q

        // think about the relationship: LCA(root), LCA(root.left), LCA(root.right)
        if (root == null) return null;
        if (root == p) return p;
        if (root == q) return q;

        TreeNode l = lowestCommonAncestor(root.left, p, q);
        TreeNode r = lowestCommonAncestor(root.right, p, q);

        if (l != null && r != null) return root; //case-1
        if (l != null && r == null) return l; //case-2
        if (l == null && r != null) return r; //case-3
        return null;
    }
}