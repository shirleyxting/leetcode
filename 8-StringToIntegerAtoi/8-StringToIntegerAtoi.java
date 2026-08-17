// Last updated: 8/16/2026, 9:53:49 PM
// class Solution {
//     public int myAtoi(String s) {
//         char[] chars = s.toCharArray();
//         int len = s.length();
//         int i = 0;
//         int sign = 1, res = 0;

//         if(len <= 0) return res;

//         // step1 - remove leading spaces
//         while(i < len && chars[i] == ' ') i ++;
//         if(i == len) return res;

//         // step2 - read +/-
//         if(chars[i] == '+') {
//             sign = 1;
//             i ++;
//         } else if(chars[i] == '-') {
//             sign = -1;
//             i ++;
//         }
//         // System.out.println(i);
//         // step3 - read any digits
//         StringBuilder numStr = new StringBuilder();
//         // remove leading '0's
//         while(i < len && chars[i] == '0') i ++;

//         while(i < len) {    
//             if(Character.isDigit(chars[i])) {
//                 numStr.append(chars[i]);
//                 i ++;
//                 res = convertToIntWithOverflowHandling(numStr.toString(), sign);
//                 // System.out.println("i = " + i);
//                 // System.out.println("numStr = " + numStr);
//             } else {
//                 return res;
//             }
//         }
//         return res;
//     }

//     private int convertToIntWithOverflowHandling(String s, int sign) {
//         if (s.length() > String.valueOf(Integer.MAX_VALUE).length()) {
//             if (sign == 1) return Integer.MAX_VALUE;
//             if (sign == -1) return Integer.MIN_VALUE;
//         }

//         long num = Long.valueOf(s);
//         num = num * sign;
//         int res;
//         if (num > Integer.MAX_VALUE) {
//             res = Integer.MAX_VALUE;
//         } else if (num < Integer.MIN_VALUE) {
//             res = Integer.MIN_VALUE;
//         } else {
//             res = (int) num;
//         }
//         return res;
//     }
// }

// method 2 - convert to num and avoid overflow, bitwise
class Solution {
    public int myAtoi(String s) {
        // i: index, total: previous total number (res = total*10 + curr_digit)
        int i = 0, sign = 1, total = 0;
        int len = s.length();

        // corner case
        if (len == 0) return 0;
        
        // 1 - remove leading spaces
        while(i < len && s.charAt(i) == ' ') i ++;
        if(i == len) return 0;

        // 2 - get the +/- sign
        if(s.charAt(i) == '+' || s.charAt(i) == '-') {
            sign = s.charAt(i) == '+' ? 1 : -1;
            i ++;
        }

        // 3 - convert to actual number and avoid overflow
        // total = total * 10 + digit -> can solve the leading 0s problem
        while(i < len && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';

            /* handle overflow, since total is generated bitwise
                total * 10 + digit > MAX -->
                - total * 10 > MAX -> total > MAX / 10
                - total = MAX/10 && digit > MAX % 10
            */
            if(total > Integer.MAX_VALUE/10 || 
                (total == Integer.MAX_VALUE/10 && digit > Integer.MAX_VALUE % 10)) {
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }

            total = total * 10 + digit;
            i ++;
        }

        return total * sign;
    }
}