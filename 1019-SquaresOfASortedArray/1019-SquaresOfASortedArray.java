// Last updated: 8/16/2026, 9:49:02 PM
class Solution {
    public int[] sortedSquares(int[] nums) {
        // int[] res = new int[nums.length];
        // for(int i = 0; i < nums.length; i ++) res[i] = nums[i] * nums[i];
        // Arrays.sort(res);
        // return res;

        // mthod 2 - two pointers
        /**
        The crux over here is that the array is already sorted.
We are comparing the first and last elements because after square these have the possibility of being the highest element.
Both the extremes contain the max element (after square ofc), so we are inserting these elements to the last of the new array to make it sorted.
 */

        int n = nums.length;
        int p1 = 0, p2 = n-1, i = n-1;
        int[] res = new int[n];
        while(p1 <= p2 && i >= 0) {
            int num1 = nums[p1], num2 = nums[p2];
            if(Math.abs(num1) > Math.abs(num2)) {
                res[i] = num1 * num1;
                p1 ++;
            } else {
                res[i] = num2 * num2;
                p2 --;
            }
            i --;
        }
        return res;
    }
}