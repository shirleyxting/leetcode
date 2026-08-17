// Last updated: 8/16/2026, 9:53:59 PM
class Solution {
    public int lengthOfLongestSubstring(String s) {
        // sliding window
        int res = 0;
        int l = 0;
        int len = s.length();

        if(len == 0 || len == 1) return len;

        // save curr window chars
        Set<Character> set = new HashSet<>();
        /*
        abcabcbb
        abc,3
        bca,3
        cab,3
        abc,3
        abcb,bcb,2, cb,2
        cbb,2 bb,1
        */
        for(int i = 0; i < len; i ++) {
            // check if curr char exist in set
            if(set.contains(s.charAt(i))) {
                // remove leftmost chars from win until no repeating chars in the win
                while(s.charAt(i) != s.charAt(l)) {
                    set.remove(s.charAt(l));
                    l++;
                }
                // now l pointer = r pointer, move l to next index
                l ++;
            } else {
                set.add(s.charAt(i));
            }
            res = Math.max(res, set.size());
        }
        return res;
    }
}