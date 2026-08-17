// Last updated: 8/16/2026, 9:51:11 PM
class Solution {
    // public boolean containsDuplicate(int[] nums) {
    //     Set<Integer> seen = new HashSet<>();
    //     for(int num: nums) {
    //         if(seen.contains(num)) return true;
    //         seen.add(num);
    //     }
    //     return false;
    // }
    
    // method 2 - sort
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for(int i = 0; i < nums.length - 1; i ++) {
            if(nums[i] == nums[i + 1]) return true;
        }
        return false;
    }
}