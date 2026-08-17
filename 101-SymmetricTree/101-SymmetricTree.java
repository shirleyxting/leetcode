// Last updated: 8/16/2026, 9:52:32 PM
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
    public boolean isSymmetric(TreeNode root) {
        // root.left == root.right
        // left.left == right.right
        // left.right == right.left
        if(root == null) return true;
        return helper(root.left, root.right);
    }

    // check if left and right is symmetric
    private boolean helper(TreeNode left, TreeNode right) {
        if(left == null && right == null) return true;
        if(left == null || right == null) return false;

        if(left.val != right.val) return false;
        return helper(left.left, right.right) && helper(left.right, right.left);
    }
    
    // // WRONG
    // public boolean isSymmetric(TreeNode root) {
    //     if(root == null) return true;
    //     if(root.left == null && root.right == null) return true;

    //     // BFS 1,2,2,3,4,4,3
    //     // pre-order:  1.2.3.4.2,4,3
    //     // in-order:   3,2,4,1,4,2,3 -> palindrome
    //     // post-order: 3,4,2,4,3,2,1
    //     // check in-order if its palindrome
    //     // WRONG!!!! [1,2,2,2,null,2] if duplicate values allowed, this is not guranteed

    //     List<Integer> inOrder = getInOrder(root);
    //     System.out.println(inOrder);
    //     int p1 = 0, p2 = inOrder.size() - 1;
    //     while(p1 < p2) {
    //         if(inOrder.get(p1) != inOrder.get(p2)) return false;
    //         p1 ++;
    //         p2 --;
    //     }
    //     if(inOrder.get(p1) != inOrder.get(p2)) return false;
        
    //     return true;
    // }

    // private List<Integer> getInOrder(TreeNode root) {
    //     List<Integer> res = new ArrayList<>();
    //     if(root == null) return res;

    //     res.addAll(getInOrder(root.left));
    //     res.add(root.val);
    //     res.addAll(getInOrder(root.right));

    //     return res;
    // }
}