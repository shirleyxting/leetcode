// Last updated: 8/16/2026, 9:52:39 PM
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
    // public boolean isSameTree(TreeNode p, TreeNode q) {
    //     // BFS, compare each node during BFS
    //     Queue<TreeNode> pQueue = new LinkedList<>();
    //     Queue<TreeNode> qQueue = new LinkedList<>();

    //     pQueue.offer(p);
    //     qQueue.offer(q);

    //     while(!pQueue.isEmpty() && !qQueue.isEmpty()) {

    //         TreeNode i = pQueue.poll();
    //         TreeNode j = qQueue.poll();

    //         if(i == null && j != null) return false;
    //         if(i != null && j == null) return false;
    //         if( (i != null && j != null) && (i.val != j.val)) return false;

    //         if(i != null) {
    //             pQueue.offer(i.left);
    //             pQueue.offer(i.right);
    //         }
    //         if(j != null) {
    //             qQueue.offer(j.left);
    //             qQueue.offer(j.right);
    //         }
    //     }

    //     if (!pQueue.isEmpty() || !qQueue.isEmpty()) return false;
    //     return true;
    // }

    // method 2 - recursion
    // p = q -> p.left=q.left, p.right=q.right, p.val = q.val
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null) return true;
        if(p != null && q == null) return false;
        if(p == null && q != null) return false;
        if(p.val != q.val) return false;

        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}