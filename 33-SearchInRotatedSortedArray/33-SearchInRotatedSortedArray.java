// Last updated: 8/16/2026, 9:53:29 PM
class Solution {
    public int search(int[] nums, int target) {
        // log(n) -> binary search
        // https://www.youtube.com/watch?v=vaGN5Cjlrfk
        int n = nums.length;
        if (n == 0) return -1;

        int l = 0, r = n - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return mid;

            // mid in left side
            // left or right -> deceide by nums[0]
            if (nums[mid] >= nums[0]) {
                if (nums[l] <= target && target <= nums[mid]) {
                    // do not forget to cover "nums[l] == target"
                    r = mid;
                } else {
                    l = mid;
                }
            } else {
            // mid in right side
                if (nums[mid] <= target && target <= nums[r]) {
                    // do not forget to cover "nums[r] == target"
                    l = mid;
                } else {
                    r = mid;
                }
            }
  
        }
        if (nums[l] == target) return l;
        if (nums[r] == target) return r;
        return -1;
    }
}