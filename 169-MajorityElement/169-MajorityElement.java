// Last updated: 8/16/2026, 9:51:56 PM
class Solution {
    // public int majorityElement(int[] nums) {
    //     Map<Integer, Integer> map = new HashMap<>();
    //     for(int num: nums) {
    //         map.merge(num, 1, (a,b) -> a+b);
    //         if(map.get(num) > nums.length/2) return num;
    //     }
    //     return -1;
    // }

    // method 2 - sort
    // if num occurs more than [n/2] times, it will always sit in the middle position [n/2] of the sorted nums
    // public int majorityElement(int[] nums) {
    //     Arrays.sort(nums);
    //     int n = nums.length;
    //     return nums[n/2];
    // }

    // method 3 - Moore's voting algorithm
    public int majorityElement(int[] nums) {
        int count = 0, candidate = 0;
        
        for(int num: nums) {
            if(count == 0) candidate = num;
            if(candidate == num) {
                count++;
            } else {
                count--;
            }
        }
        return candidate;
    }

}