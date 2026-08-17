// Last updated: 8/16/2026, 9:54:02 PM

class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*
        // 1. Brute Force
        for (int i = 0; i < nums.length; i ++) {
            for (int j = i + 1; j < nums.length; j ++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return null;
        
        // 2. HashMap - two pass
        Map<Integer, Integer> map = new HashMap<>();
        int n = nums.length;
        for (int i = 0; i < n; i ++) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < n; i ++) {
            int newTarget = target - nums[i];
            if (map.containsKey(newTarget) && map.get(newTarget) != i) {
                return new int[]{i, map.get(newTarget)};
            }
        }
        return null;
        */

        // 3.HashMap - One pass
        Map<Integer, Integer> map = new HashMap<>();
        int n = nums.length;
        for (int i = 0; i < n; i ++) {
            int newTarget = target - nums[i];
            if (map.containsKey(newTarget)) {
                return new int[]{i, map.get(newTarget)};
            }
            map.put(nums[i], i);
        }
        return null;
    }
}

