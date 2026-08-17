// Last updated: 8/16/2026, 9:53:16 PM
class Solution {
    // public List<List<Integer>> permuteUnique(int[] nums) {
    //     // backtracking
    //     List<List<Integer>> res = new ArrayList<>();
    //     boolean[] used = new boolean[nums.length];
    //     Arrays.sort(nums);
    //     helper(nums, res, new ArrayList<>(), used);
    //     return res;
    // }

    // private void helper(int[] nums, List<List<Integer>> res, List<Integer> curr, boolean[] used) {
    //     if (curr.size() == nums.length) {
    //         res.add(new ArrayList(curr)); // deep copy
    //         return;
    //     }
    //     // iterate all possible candidates
    //     for (int i = 0; i < nums.length; i ++) {
    //         if (used[i]) continue; // skip itself
    //         // skip similar value, if 1^a is used before, skip 1^b (nums is sorted)
    //         if (i > 0 && nums[i] == nums[i-1] && used[i-1]) continue;

    //         curr.add(nums[i]);
    //         used[i] = true;

    //         helper(nums, res, curr, used);

    //         curr.remove(curr.size() - 1);
    //         used[i] = false;
    //     }
    // }

    // backtracking, convert int[] nums to hashmap, key=num, val=cnt
    public List<List<Integer>> permuteUnique(int[] nums) {
        Map<Integer, Integer> numsMap = new HashMap<>();
        for (int num: nums) 
            numsMap.merge(num, 1, (a,b) -> a+b);
        
        List<List<Integer>> res = new ArrayList<>();
        helper(nums.length, numsMap, res, new ArrayList<>());
        return res;
    }

    private void helper(
        int len,
        Map<Integer, Integer> numsMap, 
        List<List<Integer>> res,
        List<Integer> curr
    ) {
        if (curr.size() == len) {
            res.add(new ArrayList(curr));
            return;
        }

        for (int key: numsMap.keySet()) {
            if (numsMap.get(key) == 0) continue; 
            curr.add(key);
            numsMap.put(key, numsMap.get(key) - 1);

            helper(len, numsMap, res, curr);

            numsMap.put(key, numsMap.get(key) + 1);
            curr.remove(curr.size() - 1);
        }
    }


}