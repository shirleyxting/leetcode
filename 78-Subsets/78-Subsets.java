// Last updated: 8/16/2026, 9:52:49 PM
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        // DFS
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        helper(nums, res, new ArrayList<>(), 0);
        return res;
    }

    private void helper(
        int[] nums, 
        List<List<Integer>> res, 
        List<Integer> subset, 
        int idx
    ) {
        // find all subsets starting with 'subset' 
        // next available number is nums[idx]

        res.add(new ArrayList<Integer>(subset)); //deep copy subset

        for(int i = idx; i < nums.length; i ++) {
            subset.add(nums[i]);
            helper(nums, res, subset, i + 1);
            subset.remove(subset.size() - 1);
        }

    }
}