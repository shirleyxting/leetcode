// Last updated: 8/16/2026, 9:53:58 PM
class Solution {
    public String longestPalindrome(String s) {
        // for each char, check left and right to expand the palindrom length
        int maxLen = 0, len = s.length();
        String res = "";
        for (int i = 0; i < len; i ++) {
            // handle odd situation, like 'abcbd' -> 'bcb'
            int l = i, r = i;
            while (l >= 0 && r < len && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > maxLen) {
                    res = s.substring(l, r + 1);
                    maxLen = r - l + 1;
                }
                l --; r ++;
            }

            // handle even chars situation, like 'cbbd' -> 'bb'
            l = i; r = i + 1;
            while (l >= 0 && r < len && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > maxLen) {
                    res = s.substring(l, r + 1);
                    maxLen = r - l + 1;
                }
                l --; r ++;
            }
        }
        return res;
    }
}