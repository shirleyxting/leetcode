// Last updated: 8/16/2026, 9:52:41 PM
class Solution {
    // public List<List<Integer>> subsetsWithDup(int[] nums) {
    //     // []
    //     // [] + [1]
    //     // [], [1] + [2`], [1, 2`]
    //     // [], [1], [2`], [1, 2`] + [2``], [1, 2``], [2`, 2``], [1, 2`, 2``]
    //     //                          skip   skip      keep      keep
    //     // for 2`` loop of 'for(List<Integer> curr : res)' 
    //     // -> skip first 2 subsets (results from nums[0]'s loop), start from [2`], [1, 2`]

    //     List<List<Integer>> res = new ArrayList<>();
    //     res.add(new ArrayList<Integer>());
    //     Arrays.sort(nums);

    //     int cachedSize = 0, startIdx = 0;
    //     for(int i = 0; i < nums.length; i ++) {
    //         List<List<Integer>> subsets = new ArrayList<>();
    //         // set startIdx before updating cachedSize
    //         // startIdx = size of previous res size
    //         startIdx = (i > 0 && nums[i] == nums[i-1]) ? cachedSize : 0;
    //         cachedSize = res.size();

    //         for(int j = startIdx; j < res.size(); j ++) {
    //             // add 'nums[i]' to each subset under 'rst'
    //             // make a deep copy of curr, 
    //             // otherwise if you add value to 'curr', the 'rst' lists will change too
    //             List<Integer> curr = res.get(j);
    //             List<Integer> temp = new ArrayList<>(curr); // deep copy
    //             temp.add(nums[i]);
    //             subsets.add(temp);
    //         }
    //         // add 'subsets' results into 'rst'
    //         // for(List<Integer> subset : subsets)
    //         //     res.add(subset);
    //         res.addAll(subsets);
    //     }
    //     return res;
    // }

    // method 2 - DFS
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        helper(res, new ArrayList<Integer>(), nums, 0);
        return res;
    }

    // return all subsets starting with 'subset', next avaible number from 'startIdx'
    // subset = [1], startIdx = 1 ->
    // [1] -> [1, 2`], [1, 2`, 2``], [1, 2``]
    // [2`] -> [2`, 2``]
    // [2``] 
    // discard [1, 2``], [2``]
    private void helper(List<List<Integer>> res, List<Integer> subset, int[] nums, int startIdx) {
        // res.add(subset); wrong, should deep copy 'subset'. otherwise 'subset will change afterwards
        res.add(new ArrayList<>(subset));

        System.out.println(subset);
        for(int i = startIdx; i < nums.length; i ++) {
            if(i > startIdx && nums[i] == nums[i - 1]) continue;
            // (i > 0 && nums[i] == nums[i - 1]) is wrong
            // cause for [1,2`,2``], it will skip the 2`` selection from {subset=[1,2`], startIdx=2}
            // so the skip should be: skip NEXT same value candidate
            // do not skip CURRENT candidate
            subset.add(nums[i]);
            // System.out.println(subset);
            helper(res, subset, nums, i + 1);
            subset.remove(subset.size() - 1);
        }

    }

}