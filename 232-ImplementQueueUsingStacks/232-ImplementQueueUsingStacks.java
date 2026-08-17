// Last updated: 8/16/2026, 9:51:05 PM
class MyQueue {
    /* [1,2,3] given [1,2] push 3
        3 should be at the bottom of stack
    1   1
    2 ->2
        3
    stack1: 1
            2
    stack1: 3, stack2: 2
                       1
    stack1: 3, push 2, push 1 
    */
    private Stack<Integer> s1, s2;
    // s1 is the stack saves actual values
    private int front;
    // front value is saved as a const, and be modified during push/pop

    public MyQueue() {
        s1 = new Stack<>();
        s2 = new Stack<>();
    }
    
    public void push(int x) {
        if(s1.isEmpty()) front = x;
        while(!s1.isEmpty()) {
            s2.push(s1.pop());
        }
        s1.push(x);
        while(!s2.isEmpty()) {
            s1.push(s2.pop());
        }
    }
    
    public int pop() {
        int res = s1.pop();
        if(!s1.isEmpty()) front = s1.peek();
        return res;
    }
    
    public int peek() {
       return front;
    }
    
    public boolean empty() {
        return s1.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */