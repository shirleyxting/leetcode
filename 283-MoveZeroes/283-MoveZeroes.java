// Last updated: 8/16/2026, 9:50:43 PM
class Solution {
    public void moveZeroes(int[] nums) {
        /*
        0,1,0,3,12
        1,3,12,0,0

        int nonZeos = records # of non-0
        make nums[0~nonZeros] to nonZeros, and left as 0
        */
        int nonZeros = 0;
        for(int num: nums) {
            if(num != 0) {
                nums[nonZeros] = num;
                nonZeros ++;
            }
        }

        if(nonZeros > 0) {
            for(int i = nonZeros; i < nums.length; i ++) {
                nums[i] = 0;
            }
        }
    }
}