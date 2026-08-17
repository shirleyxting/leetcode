// Last updated: 8/16/2026, 9:53:36 PM
class Solution {
    public boolean isValid(String s) {
        int n = s.length();
        if(n % 2 == 1) return false;

        // we only have 3 cases here, no need to create a map to save the match relationship
        // directly list the possible cases, will simplify the codes
        Stack<Character> stack = new Stack<>();
        for(char c: s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else {
                // c is close parenthese, compare with stack.peek
                if (stack.empty()) {
                    return false;
                } 
                char c_ = stack.peek();
                if( (c_ == '(' && c == ')') ||
                    (c_ == '{' && c == '}') ||
                    (c_ == '[' && c == ']') ) {
                        stack.pop();
                } else {
                    return false;
                }
            }
        }
        // return stack.size() == 0;
        return stack.empty();


        
        // Map<Character, Character> map = new HashMap<>();
        // map.put('(', ')');
        // map.put('{', '}');
        // map.put('[', ']');
        // // FILO, if current c matches stack.peek, then pop it and check to next c
        // Stack<Character> stack = new Stack<>();
        // for(int i = 0; i < n; i ++) {
        //     char c = s.charAt(i);
        //     if ( stack.empty() ) {
        //         stack.push(c);
        //     } else if ( !map.containsKey(stack.peek())) {
        //         return false; 
        //         // stack only contains the open parenthese, 
        //         // if closed parenthese is in stack, then return false
        //     } else if (map.get(stack.peek()) != c) {
        //         stack.push(c);
        //     } else {
        //         stack.pop();
        //     }
        // }
        // return stack.size() == 0;
    }
}