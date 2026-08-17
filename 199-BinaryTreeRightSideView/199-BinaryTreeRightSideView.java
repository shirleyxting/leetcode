// Last updated: 8/16/2026, 9:51:25 PM
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
    public List<Integer> rightSideView(TreeNode root) {
        // append each layer's most right node -> BFS
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()) {
            // List<Integer> temp = new ArrayList<>();
            int qSize = queue.size();
            for(int i = 0; i < qSize; i ++) {
                TreeNode curr = queue.poll();
                // temp.add(curr.val);
                // the last node will be saved into "temp"
                if (i == qSize - 1) res.add(curr.val);
                
                if(curr.left != null) queue.offer(curr.left);
                if(curr.right != null) queue.offer(curr.right);
            }
            // res.add(temp.get(temp.size() - 1));
        }

        return res;
    }
}