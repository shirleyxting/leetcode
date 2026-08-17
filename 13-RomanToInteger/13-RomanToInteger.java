// Last updated: 8/16/2026, 9:53:47 PM
class Solution {
    public int romanToInt(String s) {
        if(s.isEmpty()) return 0;
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        
        int res = 0;
        for(int i = 0; i < s.length() - 1; i ++) {
            int currInt = map.get(s.charAt(i));
            if( map.get(s.charAt(i)) < map.get(s.charAt(i+1)) ) {
                currInt = currInt * (-1);
            }
            res += currInt;
        }
        res += map.get(s.charAt(s.length() - 1));

        return res;

        // // if current character 'c_i' < ''c_i+1', then distract c_i
        // int res = 0;
        // for (int i = 0; i < s.length() - 1; i ++) {
        //     if(map.get(s.charAt(i)) < map.get(s.charAt(i + 1))) {
        //         res -= map.get(s.charAt(i));
        //     } else {
        //         res += map.get(s.charAt(i));
        //     }
        // }
        // res += map.get(s.charAt(s.length() - 1));
        // return res;
    }
}