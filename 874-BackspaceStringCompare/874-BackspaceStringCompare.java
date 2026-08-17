// Last updated: 8/16/2026, 9:49:20 PM
class Solution {
    public boolean backspaceCompare(String s, String t) {
        // FILO, Stack
        Stack<Character> s1 = new Stack<>(), s2 = new Stack<>();
        for(char c: s.toCharArray()) {
            if(c == '#' && !s1.isEmpty()) {
                s1.pop();
            } else if(c == '#' && s1.isEmpty()) {
                continue;
            } else {
                s1.push(c);
            }
        }
        for(char c: t.toCharArray()) {
            if(c == '#'&& !s2.isEmpty()) {
                s2.pop();
            } else if(c == '#' && s2.isEmpty()) {
                continue;
            } else {
                s2.push(c);
            }
        }
        return s1.equals(s2);
    }
}