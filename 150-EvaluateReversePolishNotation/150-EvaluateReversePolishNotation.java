// Last updated: 8/16/2026, 9:51:57 PM
class Solution {
    public int evalRPN(String[] tokens) {
        // reverse polish notation: operator comes after operands
        // 3 + 4 -> 3 4 +
        // stack, pop 2 numbers, compute the value with operator, then push results back to stack
        Stack<Integer> stack = new Stack<>();
        for(String s: tokens) {
            if (s.equals("+")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a + b);
            } else if (s.equals("-")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a - b);
            } else if (s.equals("*")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a * b);
            } else if (s.equals("/")) {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(a / b);
            } else {
                stack.push(Integer.valueOf(s));
            }
        }
        return stack.pop();
    }
}