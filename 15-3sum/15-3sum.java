// Last updated: 8/16/2026, 9:53:38 PM
class Solution {
    // public List<List<Integer>> threeSum(int[] nums) {
    //     // convert to 2-sum: i+j = -k
    //     Set<List<Integer>> res = new HashSet<>();
    //     int n = nums.length;
        
    //     Arrays.sort(nums);

    //     for (int i = 0; i < n-2; i ++) {
    //         if(i > 0 && nums[i] == nums[i-1]) continue;
            
    //         int target = 0 - nums[i];
    //         Set<Integer> set = new HashSet<>();
    //         for (int j = i + 1; j < n; j ++) {
    //             int newTarget = target - nums[j];
    //             if (set.contains(newTarget)) {
    //                 res.add(Arrays.asList(nums[i], newTarget, nums[j]));
    //             } else {
    //                 set.add(nums[j]);
    //             }
    //         }
    //     }
    //     return new ArrayList<>(res);
    // }

    // convert to 2-sum, two pointer, remove duplicate by jump to next differnt number
    public List<List<Integer>> threeSum(int[] nums) {
        int n = nums.length;
        List<List<Integer>> res = new ArrayList<>();

        Arrays.sort(nums);

        for(int i = 0; i < n - 2; i ++) {
            int target = -nums[i];
            int left = i + 1, right = n - 1;
            // remove duplicate nums[i]
            if(i > 0 && nums[i] == nums[i-1]) continue;

            while(left < right) {
                int sum = nums[left] + nums[right];
                if(sum == target) {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++; right--;
                    // remove duplicate nums[left]
                    while(left < right && nums[left] == nums[left-1]) left++;
                    // remove duplicate nums[right]
                    while(left < right && nums[right] == nums[right+1]) right--;

                } else if (sum < target) {
                    left ++;
                } else {
                    right --;
                }    
            }
        }
        return res;
    }
}