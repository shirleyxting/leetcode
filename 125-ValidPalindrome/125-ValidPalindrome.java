// Last updated: 8/16/2026, 9:52:21 PM
class Solution {
    public boolean isPalindrome(String s) {
        // // replace non-alphanumeric chars to empty
        // String newS = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        // System.out.println(newS);
        // int n = newS.length();
        // int p1 = 0, p2 = n - 1;
        // while(p1 < n / 2) {
        //     if (newS.charAt(p1) != newS.charAt(p2)) return false;
        //     p1 ++;
        //     p2 --;
        // }
        // return true;

        // or without regex
        int p1 = 0, p2 = s.length() - 1;
        while(p1 <= p2) {
            if ( !Character.isLetterOrDigit(s.charAt(p1)) ) {p1++; continue;}
            if ( !Character.isLetterOrDigit(s.charAt(p2)) ) {p2--; continue;}
            if ( Character.toLowerCase(s.charAt(p1)) != Character.toLowerCase(s.charAt(p2)) ) return false;
            p1 ++;
            p2 --;
        }
        return true;
    }
}