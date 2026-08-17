// Last updated: 8/16/2026, 9:51:42 PM
public class Solution {
    // you need to treat n as an unsigned value

    // public int hammingWeight(int n) {
    //     // if n is postigve:
    //     // if n is even, 
    //     // 2,4,8,16: all have only count of '1' = 1
    //     // 3 (11), 6 (110), 12 (1100): all have same count of '1'
    //     // if n is odd
    //     // 1(1),3(11),7(111),15(1111): n - count of '1' = n/2 - count of '1' + 1
    //     // 5(101), 11(1011), 23 (10111)
    //     // 4(100), 9(1001), 19(10011)

    //     // if n is negative
    //     // -1 = unsigned binary of 2^32 - 1
    //     // -2 =                    2^32 - 2
    //     // -2^16 =                 2^32 - 2^16

    //     // input is a binary string of length 32, 
    //     // n can only be [-2^16, 2^16)

    //     if (n >= 0) {
    //         if(n == 0 || n == 1) return n;
    //         if(n % 2 == 0) return hammingWeight(n/2);
    //         if(n % 2 == 1) return hammingWeight(n/2) + 1;
    //     } else {
    //         System.out.println(n);
    //         System.out.println(Math.pow(2, 32));
    //         System.out.println((int)Math.pow(2, 32));
    //         // java int: 32bit but its using 2's complement notation,
    //         // so java int [-2^16, 2^16]
    //         System.out.println((long)Math.pow(2, 32));
    //         long unsignedN = (long)(Math.pow(2, 32)) + n;
    //         System.out.println(unsignedN);
    //         return helper(unsignedN);
    //     }

    //     return -1;
    // }

    // private int helper(long n) {
    //     if(n == 0 || n == 1) return (int) n;
    //     if(n % 2 == 0) return helper(n/2);
    //     if(n % 2 == 1) return helper(n/2) + 1;
    //     return -1;
    // }

    // method 2 - bit operation
    // n & 1 (000...0001) -> the last bit of n is 1 or 0
    // check solution for: 
    // >>  (signed bitwise right shift)
    // >>> (unsigned                  )
    // in java, the leftmost bit means the sign (positive[0...] or negative[1...])
    public int hammingWeight(int n) {
        if(n == 0) return 0;

        int res = 0;
        while( n != 0 ) {
            // if the last bit is 1, add 1 to res
            res += n & 1;

            // bitwise unsigned right shift, move 1 step to right
            n = n >>> 1;
        }
        return res;
    }
}