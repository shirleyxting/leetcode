// Last updated: 8/16/2026, 9:54:03 PM
object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        var result = Array(0, 0) // initiate 'result' array with number 0
        for (i <- 0 to (nums.size - 1)) {
            for (j <- (i+1) to (nums.size - 1)) {
                if (nums(i) + nums(j) == target) {
                    result = Array(i, j)
                }
            }
        }
        result
    }
}