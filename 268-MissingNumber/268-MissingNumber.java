// Last updated: 8/16/2026, 9:50:44 PM
class Solution {
    public int missingNumber(int[] nums) {
        // int n = nums.length;
        // Arrays.sort(nums);
        // for(int i = 0; i < n ; i ++) {
        //     if(nums[i] != i) return i;
        // }
        // return n;

        // // method 2 - hashSet
        // int n = nums.length;
        // Set<Integer> set = new HashSet<>();
        // for(int num: nums) set.add(num);
        // for(int i = 0; i <= n; i ++) {
        //     if(!set.contains(i)) return i;
        // }
        // return -1;

        // // method 3 - Math
        // // (1+2+3) - (1+2) = 3 (missing number)
        // int n = nums.length;
        // int sum1 = (int) (1+n)*n/2;
        // int sum2 = 0;
        // for(int num: nums) sum2 += num;
        // return sum1 - sum2;

        // method 4 - bit operation - xor
        // a^b^b = a
        // xor of index [0~n] and nums[i]
        // a^c^b^d^b^a^d = a^a^b^b^d^d^c = c (the missing one)
        int xor = 0;
        int n = nums.length;
        for(int i = 0; i < n; i ++) {
            xor = xor ^ i ^ nums[i];
        }
        int res = xor ^ n;
        return res;
    }
}