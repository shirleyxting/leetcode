// Last updated: 8/16/2026, 9:50:32 PM
class Solution {
    // public int[] countBits(int n) {
    //     /*
    //     0 --> 0                         0
    //     1 --> 1 = 2^0                   1
    //     2 --> 10 = 2^1                  1
    //     3 --> 11 = 2^1 + 1              2   
    //     4 --> 100 = 2^2                 1
    //     5 --> 101 = 2^2 + 1             2
    //     6 --> 110 = 2^2 + 2^1           2     
    //     7 --> 111 = 2^2 + 2^1 + 1       3
    //     8 --> 1000 = 2^4                1
    //     9 --> 1001                      2
    //     10--> 1010                      2
    //     11--> 1011                      3
    //     12--> 1100                      2
    //     13--> 1101                      3
    //     14--> 1110                      3
    //     15--> 1111                      4
    //     16--> 10000                     1

    //     2,4,8,16,..., i, 2*i : binary representation of 2*i = binary representation of i, append 0 to the end
    //     3,6,12: same, 2*i = i, appends 0 to the end
    //     -> for even number 2*i, the '1' count = the '1' count of binary representation i

    //     1,3,7,15, i, 2*i+1: binary_[2*i+1] = bianry_[i], append 0 to the end, add '1'
    //     same situation for: 5,11
    //     -> for odd number 2*i+1, the '1' count = the '1' count of binay_[i] + 1

    //     Summary:
    //     binay representation,
    //     if you append 0 to the end, euqals to multiply the number with 2
    //     */

    //     int[] res = new int[n+1];
    //     for(int i = 0; i <=n; i ++) {
    //         res[i] = helper(i);
    //     }
    //     return res;
    // }

    // private int helper(int num) {
    //     // get the count of '1' of binary representation of num
    //     if(num == 0) return 0;
    //     if(num == 1) return 1;

    //     if(num % 2 == 0) return helper(num/2);
    //     if(num % 2 == 1) return helper(num/2) + 1;
    //     return -1;
    // }

    // method 2 - add memorization memo[] to record the '1' count for number i
    // cause it will re-call helper() many times
    public int[] countBits(int n) {
        int[] res = new int[n+1];
        
        for(int i = 0; i <= n; i ++) {
            res[i] = helper(i, res);
        }
        return res;
    }

    private int helper(int num, int[] memo) {
        if(num == 0 || num == 1) return num;

        // check if num already calculated in memo[], er will re-use it
        if(memo[num] != 0) return memo[num];

        if(num % 2 == 0) memo[num] = helper(num/2, memo);
        if(num % 2 == 1) memo[num] = helper(num/2, memo) + 1;
        return memo[num];
    }
}