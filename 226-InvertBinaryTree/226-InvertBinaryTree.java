// Last updated: 8/16/2026, 9:51:09 PM
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
    // public TreeNode invertTree(TreeNode root) {
    //     if(root == null)  return root;
    //     // recursive exit
    //     if(root.left == null && root.right == null) return root;
    //     TreeNode res = new TreeNode();
        
    //     // divide and conquer
    //     // invert(root) = root.val + invert(left) + invert(right)
    //     res.val = root.val;
    //     res.left = invertTree(root.right);
    //     res.right = invertTree(root.left);
            
    //     return res;
    // }

    // BFS
    public TreeNode invertTree(TreeNode root) {
        if(root == null) return null;
        Queue<TreeNode> queue = new LinkedList<>();

        queue.offer(root);
        while(!queue.isEmpty()) {
            TreeNode curr = queue.poll();
            if(curr.left != null) queue.offer(curr.left);
            if(curr.right != null) queue.offer(curr.right);

            // invert curr left and right child
            TreeNode temp = curr.left;
            curr.left = curr.right;
            curr.right = temp;
        }
        return root;
    }
}