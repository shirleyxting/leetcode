// Last updated: 8/16/2026, 9:53:23 PM
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        // DFS to get all combinations

        Arrays.sort(candidates);
        List<List<Integer>> res = new ArrayList<>();
        helper(candidates, target, 0, res, new ArrayList<>());
        return res;
    }

    // get a combination with sum = target, 
    // candidates starts from nums[idx]
    // avaiable candidates are nums[idx: ]
    private void helper(
        int[] nums, int target, int idx,
        List<List<Integer>> res, 
        List<Integer> comb) {
        if (target < 0) return;
        if (target == 0) {
            // System.out.println(comb);
            res.add(new ArrayList(comb)); // make deep copy of 'comb'
            // System.out.println(res);
            return;
        }

        // iterate all possible candidates
        for (int i = idx; i < nums.length; i ++) {
            comb.add(nums[i]); // add candidate
            helper(nums, target - nums[i], i, res, comb);
            comb.remove(comb.size() - 1); // remove just added candidate
        }

        
    }
}