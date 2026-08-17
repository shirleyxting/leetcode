// Last updated: 8/16/2026, 9:53:45 PM
class Solution {
    public boolean isPalindrome(int x) {
        // String num = String.valueOf(x);
        // String reverseNum = new StringBuilder(num).reverse().toString();
        // return num.equals(reverseNum);

        // without converting to string, compare by digits
        // and remeber cannot change the values of x
        if(x < 0) return false;
        if(x == 0) return true;
        int num = x, newNum = 0;
        while(num != 0) {
            int mod = num % 10;
            newNum = newNum * 10 + mod;
            num = num / 10;
        }
        return x == newNum;
        // 1234
        // 4*10+3 = 43
        // 43*10+2 = 432
    }
}