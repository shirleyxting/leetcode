// Last updated: 8/16/2026, 9:51:58 PM
// class MinStack {
//     // each stack node has a minVal, minVal is the min pushed so far in stack
//     private ArrayList<Integer> minList; 
//     private int minVal;
//     private Stack<Integer> stack;
//     public MinStack() {
//         stack = new Stack<>();
//         minList = new ArrayList<>();
//         minVal = Integer.MAX_VALUE;
//     }
    
//     public void push(int val) {
//         // if stack is empty, refresh the minVal as the max integer
//         if (stack.isEmpty()) minVal = Integer.MAX_VALUE;
//         stack.push(val);

//         if (minList.isEmpty()) {
//             minVal = val;
//         } else {
//             int currMin = minList.get(minList.size() - 1);
//             minVal = Math.min(currMin, val);
//         }
        
//         minList.add(minVal);
//     }
    
//     public void pop() {
//         stack.pop();
//         minList.remove(minList.size() - 1);
//         // System.out.println(minList);
//     }
    
//     public int top() {
//         return stack.peek();
//     }
    
//     public int getMin() {
//         return minList.get(minList.size() - 1);
//     }
// }

// method 2 - use another stack to save the current min value
// when pop, pop from both 2 stacks to keep min val up-to-date
class MinStack {
    Stack<Integer> stack = new Stack<>();
    Stack<Integer> minStack = new Stack<>();

    public void push(int val) {
        stack.push(val);
        int min = minStack.isEmpty() ? val : Math.min(val, minStack.peek());
        minStack.push(min);
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */