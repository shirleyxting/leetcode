// Last updated: 8/16/2026, 9:50:53 PM
class Solution {
    // public boolean isAnagram(String s, String t) {
    //     if(s.length() != t.length()) return false;
    //     // if the map of (char, occurance count) is the same, then TRUE
    //     Map<Character, Integer> mapS = new HashMap<>();
    //     Map<Character, Integer> mapT = new HashMap<>();

    //     // for(char c: s.toCharArray()) {
    //     //     mapS.merge(c, 1, (a,b) -> a+b);
    //     // }
    //     // for(char c: t.toCharArray()) {
    //     //     mapT.merge(c, 1, (a,b) -> a+b);
    //     // }
    //     // no need for 2 loops, use 1 instead, cause the length of s, t should match
    //     for(int i = 0; i < s.length(); i ++) {
    //         mapS.merge(s.charAt(i), 1, (a,b) -> a+b);
    //         mapT.merge(t.charAt(i), 1, (a,b) -> a+b);
    //     }
    //     return mapS.equals(mapT);
    // }

    // method 2, convert to char SORTED array, then comapre arrays
    public boolean isAnagram(String s, String t) {
        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();

        Arrays.sort(sChars);
        Arrays.sort(tChars);

        return Arrays.equals(sChars, tChars);
    }
}