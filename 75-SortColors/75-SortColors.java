// Last updated: 8/16/2026, 9:52:51 PM
class Solution {
    // public void sortColors(int[] nums) {
    //     int cnt0, cnt1, cnt2;
    //     cnt0 = cnt1 = cnt2 = 0;
    //     int n = nums.length;
    //     for (int i = 0; i < n; i ++) {
    //         if(nums[i] == 0) cnt0++;
    //         if(nums[i] == 1) cnt1++;
    //         if(nums[i] == 2) cnt2++;
    //     }
    //     for (int i = 0; i < cnt0; i ++) nums[i] = 0;
    //     for (int i = cnt0; i < cnt0+cnt1; i ++) nums[i] = 1;
    //     for (int i = cnt0+cnt1; i < n; i ++) nums[i] = 2;     
    // }

    // two pointers
    // nums on the left side of 'l': = 0
    //             right        'r': = 2
    // another iterator i to swap number
    public void sortColors(int[] nums) {
        int n = nums.length;
        int l = 0, r = n - 1, i = 0;
        while(i <= r) {
            if(nums[i] == 0) {
                swap(nums, i, l);
                l++;
            } else if (nums[i] == 2) {
                swap(nums, i, r);
                r --;
                i --;
                // i should keep unchanged, cause we may swap 0 to nums_i
                // so current i will be compare again with 'l'
            }
            i ++;
        }
    }

    // swap nums[i] and nums[j] in-pace
    public void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}