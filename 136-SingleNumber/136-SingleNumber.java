// Last updated: 8/16/2026, 9:52:15 PM
class Solution {
    public int singleNumber(int[] nums) {
        // Arrays.sort(nums);
        // // 1,2,2,3,3 -> i != i+1, return i
        // // 1,1,2,3,3 -> i == i+1, i+=2, return i
        // // 1,1,2,2,3
        // int i = 0;
        // while(i < nums.length - 1) {
        //     if(nums[i] != nums[i + 1]) {
        //         return nums[i];
        //     } else {
        //         i += 2;
        //     }
        // }
        // return nums[i];

        // // method 2 - XOR bitwise
        // // 0^a = a, a^a = 0, a^a^a = a
        // // a^b^c^a^c = a^a^c^c^b  = 0^b = b
        // int res = 0;
        // for(int num: nums) {
        //     res = res^num;
        // }
        // return res;

        // method 3 - math, sum
        // save all UNIQUE number to set
        // sum1 = a+a+c+c+b = 2*(a+c) + b
        // sum2 = 2*SET = 2*(a+c+b)
        // sum2 - sum1 = res
        Set<Integer> set = new HashSet<>();
        int sum1 = 0, sum2 = 0;
        for(int num: nums) {
            set.add(num);
            sum1 += num;
        }
        for(int n: set) {
            sum2 += n;
        }
        return 2*sum2 - sum1;
    }
}