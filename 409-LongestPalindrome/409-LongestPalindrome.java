// Last updated: 8/16/2026, 9:50:24 PM
class Solution {
    // public int longestPalindrome(String s) {
    //     // a-1, b-1. c-4, d-2, e-5, f-3
    //     //   ccdeefefeedcc - all 'c','d', 2'f', 5'e', 0'a', 0'b'
    //     // get all even char, and all odd char, with cnt-1 occurence, and one odd char with cnt occurence
    //     // i.e., we use ALL chars, except for each odd-count char we must leave one, except one odd char we can use all of it
    //     int res = 0;
    //     Map<Character, Integer> map = new HashMap<>();

    //     for(char c: s.toCharArray()) {
    //         map.merge(c, 1, (a,b) -> a+b);
    //     }
    //     for(char c: map.keySet()) {
    //         if (map.get(c) % 2 == 0) {
    //             res += map.get(c);
    //         } else {
    //             res += map.get(c) - 1;
    //         }
    //     }
    //     return res + 1;
    // }

    // OR: res = s.length() - (the count of odd chars) + 1 (if exist odd char)
    //         = s.length() (if do NOT exist odd char)
    public int longestPalindrome(String s) {
        int res = 0;
        Set<Character> oddChars = new HashSet<>();

        for(char c: s.toCharArray()) {
            if (oddChars.contains(c)) {
                oddChars.remove(c);
            } else {
                oddChars.add(c);
            }
        }

        if (oddChars.isEmpty()) return s.length();
        res = s.length() - oddChars.size() + 1;
        return res;
    }
}