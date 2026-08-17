// Last updated: 8/16/2026, 9:53:44 PM
class Solution {
    public String longestCommonPrefix(String[] strs) {
        // compare first string with remaining strings
        if(strs.length == 0) return "";
        if(strs.length == 1) return strs[0];
        String s1 = strs[0];
        int len1 = s1.length();
        StringBuilder res = new StringBuilder(len1); // LCA: max is the s1
        
        for(int j = 0; j < len1; j ++) {
            // compare string with s1, by char at index j
            char c = s1.charAt(j);
            for(int i = 1; i < strs.length; i ++) {
                // compare s1 with remaining strings

                if(strs[i].length() <= j || c != strs[i].charAt(j)) {
                    return res.toString();
                } 
            }
            res.append(s1.charAt(j));
        }
        return res.toString();
    }
}