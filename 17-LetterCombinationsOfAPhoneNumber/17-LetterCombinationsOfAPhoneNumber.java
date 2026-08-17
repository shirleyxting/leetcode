// Last updated: 8/16/2026, 9:53:33 PM
class Solution {
    private Map<Character, String> map = new HashMap<>();
    public List<String> letterCombinations(String digits) {
        // digits[i] will only be [2,9]
        List<String> res = new ArrayList<>();
        if(digits.length() == 0) return res;

        // get a map: digit - string
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");

        // get all combinations -> DFS
        getCombinations(new StringBuilder(), digits, 0, res);
        
        return res;
    }

    // get all possible strings starting with 'curr', next available char are from digits[idx]
    private void getCombinations(StringBuilder curr, String digits, int idx, List<String> res) {

        if(idx == digits.length()) {
            res.add(curr.toString());
            return;
        }
        String chars = map.get(digits.charAt(idx));
        for(char c : chars.toCharArray()) {
            curr.append(c);
            getCombinations(curr, digits, idx + 1, res);
            curr.deleteCharAt(curr.length() - 1);
        }
    }

}