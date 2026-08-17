// Last updated: 8/16/2026, 9:53:18 PM
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        // DFS - all permutations
        List<List<Integer>> res = new ArrayList<>();
        dfs(nums, res, new ArrayList<>());
        return res;
    }

    private void dfs(int[] nums, List<List<Integer>> res, List<Integer> curr) {
        if (curr.size() > nums.length) return;
        if (curr.size() == nums.length) {
            res.add(new ArrayList(curr)); // deep copy
            return;
        }

        // iterate all possible candidates
        for (int i = 0; i < nums.length; i ++) {
            // skip already added candidates 
            if (curr.contains(nums[i])) continue;
            
            curr.add(nums[i]);
            dfs(nums, res, curr);
            curr.remove(curr.size() - 1);
        }
    }
}