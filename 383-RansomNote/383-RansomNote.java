// Last updated: 8/16/2026, 9:50:25 PM
class Solution {
    // public boolean canConstruct(String ransomNote, String magazine) {
    //     // hashmap, get char and occurence
    //     Map<Character, Integer> map1 = new HashMap<>();
    //     Map<Character, Integer> map2 = new HashMap<>();

    //     for(char c : ransomNote.toCharArray()) {
    //         map1.merge(c, 1, (a,b) -> a+b);
    //     }
    //     for(char c : magazine.toCharArray()) {
    //         map2.merge(c, 1, (a,b) -> a+b);
    //     }
    //     for(char c : map1.keySet()) {
    //         if (map2.containsKey(c) && map2.get(c) >= map1.get(c)) {
    //             continue;
    //         } else {
    //             return false;
    //         }
    //     }
    //     return true;
    // }

    // method 2 - keep only map2, if find c in ransomNote, then reduce the value by 1
    // public boolean canConstruct(String ransomNote, String magazine) {
    //     // hashmap, get char and occurence
    //     Map<Character, Integer> map = new HashMap<>();

    //     for(char c : magazine.toCharArray()) {
    //         map.merge(c, 1, (a,b) -> a+b);
    //     }
    //     for(char c : ransomNote.toCharArray()) {
    //         if ( !map.containsKey(c) || map.get(c) <= 0 ) return false;
    //         // if current count of 'c' <= 0, then it will become negative -> false
    //         // map.merge(c, -1, (a,b) -> a+b);  OR:
    //         map.put(c, map.get(c) - 1);

    //     }
    //     return true;
    // }

    // method 3 - since it only contains lowercase english letter, replace map with int[26] 
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] charCnt = new int[26];
        
        for (char c: magazine.toCharArray()) {
            charCnt[c - 'a'] ++;
        }

        for (char c: ransomNote.toCharArray()) {
            if (charCnt[c - 'a'] <= 0) return false;
            charCnt[c - 'a'] --;
        }
        return true;
    }
}