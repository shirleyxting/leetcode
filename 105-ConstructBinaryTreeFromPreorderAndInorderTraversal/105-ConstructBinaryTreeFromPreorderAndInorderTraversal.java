// Last updated: 8/16/2026, 9:52:25 PM
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
// class Solution {
//     public TreeNode buildTree(int[] preorder, int[] inorder) {
//         // 1st num in preorder is ROOT
//         // find the 'root' index, 'mid', in 'inorder', 
//         // before the 'mid' index is LEFT_SUBTREE, after the 'mid' index is RIGHT_SUBTREE
//         // and then recursively!
//         // the preorder[1 : mid+1), inorder[ : mid) -> makes LEFT_SUBTREE
//         // the preorder[mid+1 : ], inorder[mid+1 : ] -> makes RIGHT_SUBTREE

//         // exit case
//         if(preorder.length == 0 && inorder.length == 0) return null;

//         TreeNode root = new TreeNode(preorder[0]);
//         // find the index of 'root' in inorder
//         int mid = 0;
//         for(int i = 0; i < inorder.length; i ++) {
//             if(inorder[i] == root.val) {
//                 mid = i;
//                 break;
//             }
//         }

//         root.left = buildTree(
//             Arrays.copyOfRange(preorder, 1, mid+1),
//             Arrays.copyOfRange(inorder, 0, mid)
//             );
        
//         root.right = buildTree(
//             Arrays.copyOfRange(preorder, mid+1, preorder.length),
//             Arrays.copyOfRange(inorder, mid+1, inorder.length)
//             );

//         return root;
//     }
// }

// Arrays.copyOfRange take extra time...
// create a helper func and pass index as parameter, instead of the arrary
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // pass indexMap to speed up index find
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < inorder.length; i ++) {
            map.put(inorder[i], i);
        }
        return helper(preorder, inorder, 0, preorder.length - 1, 0, inorder.length-1, map);
    }

    private TreeNode helper(int[] preorder, int[] inorder, 
        int preStart, int preEnd, int inStart, int inEnd,
        Map<Integer, Integer> map
        ) {
        // exit case
        if(preStart > preEnd || inStart > inEnd) return null;

        TreeNode root = new TreeNode(preorder[preStart]);
        // find root's index in 'inorder'
        int mid = map.get(root.val);
        int leftTreeLen = mid - inStart;

        root.left = helper(preorder, inorder, 
            preStart+1, preStart + leftTreeLen, inStart, mid-1, map);
        root.right = helper(preorder, inorder, 
            preStart + leftTreeLen + 1, preEnd, mid+1, inEnd, map);
        return root;

    }
}
