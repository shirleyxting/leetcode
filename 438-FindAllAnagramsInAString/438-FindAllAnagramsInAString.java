// Last updated: 8/16/2026, 9:50:13 PM
class Solution {
    // public List<Integer> findAnagrams(String s, String p) {
    //     // Brute Force -- TLE
    //     List<Integer> res = new ArrayList<>();
    //     if(s.length() < p.length()) return res;

    //     for(int i = 0; i <= s.length() - p.length(); i ++) {
    //         String curr = s.substring(i, i + p.length());
    //         if(isAnagram(curr, p)) res.add(i);
    //     }
    //     return res;
    // }

    // private boolean isAnagram(String a, String b) {
    //     Map<Integer, Integer> map = new HashMap<>();
    //     a.chars().forEach(
    //         c -> map.put(c, map.getOrDefault(c, 0) + 1)
    //     );
    //     b.chars().forEach(
    //         c -> map.put(c, map.getOrDefault(c, 0) - 1)
    //     );
    //     for(int v: map.values()) {
    //         if(v != 0) return false;
    //     }
    //     return true;
    // }

    // sliding window
    public List<Integer> findAnagrams(String s, String p) {
        // sliding window to reduce computations
        int[] sCount = new int[26];
        int[] pCount = new int[26];
        int pLength = p.length(), sLength = s.length();
        List<Integer> res = new ArrayList<>();
        
        if(sLength < pLength) return res;
        
        // prepare pCount for anagram comparison
        for(int i = 0; i < pLength; i ++) {
            pCount[p.charAt(i) - 'a'] ++;
            sCount[s.charAt(i) - 'a'] ++; // init window
        }
        // check if init window satisfies anagram
        if (isAnagram(sCount, pCount)) res.add(0);
        
        // sliding window, i: right pointer
        for(int i = pLength; i < sLength; i ++) {
            // remove leftmost char from window
            sCount[s.charAt(i - pLength) - 'a'] --;
            // add curr char into window
            sCount[s.charAt(i) - 'a'] ++;
            // check anagram
            if(isAnagram(sCount, pCount)) res.add(i - pLength + 1);
        }
        return res;
    }
    
    private boolean isAnagram(int[] a, int[] b) {
        if(a.length != 26 || b.length != 26) return false;
        for (int i = 0; i < 26; i ++) {
            if (a[i] != b[i]) return false;
        }
        return true;
    }
}