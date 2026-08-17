// Last updated: 8/16/2026, 9:51:37 PM
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        /*
        0000 0010 1001 0100  0001 1110 1001 1100
        0011 1001 0111 1000  0010 1001 0100 0000
        reverse: head->tail, tail->head
        0 & 1 = 0, 1 & 1 = 1
        use & to get the current bit of 'n', push it to 'result'
        'result' will left shift every round
        'n'           right
        */
        if(n == 0) return 0;
        int res = 0;
        // while(n != 0) { WRONG, cause the move must be exact 32 times, if n= 0001...1, then the move will < 32 times
        for(int i = 0; i < 32; i ++) {
            res = res << 1; // left shift first to make the last binary bit position avaiable 
            res += n & 1;
            // if n&1=1, means the last binary bit of 'n' is 1, which will cause res + 1
            // if n&1=0,                                     0,                        0         
            n = n >>> 1;
            // System.out.println(n);
        }
        return res;
    }
}