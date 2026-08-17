// Last updated: 8/16/2026, 9:51:03 PM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        // // linkedList is queue, FIFO
        // // Stack, LIFO
        // // comapre queue and stack one by one -> palindrome order

        // Stack<Integer> stack = new Stack<>();
        // ListNode curr = head;
        // while( curr != null) {
        //     stack.push(curr.val);
        //     curr = curr.next;
        // }
        
        // while(head != null) {
        //     if(head.val != stack.peek()) {
        //         return false;
        //     } else {
        //         head = head.next;
        //         stack.pop();
        //     }
        // }
        // return true;

        // method 2 - Floyd's Cycle, check marked solution for expalnation
        // when fast reades end (fast == null || fast.next == null), slow is at MIDDLE
        // reverse the back half of the list with a 'prev' node,
        // so they points to prev, instead of next
        // after reversing, slow is at the end
        // restart fast from the begin
        // compare begin vs. end
        if(head == null || head.next == null) return true;
        ListNode fast = head, slow = head;
        ListNode prev, temp;
        while(fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        
        // reverse the back half of linkedList
        prev = slow;
        slow = slow.next;
        prev.next = null; // middle points to null, avoid cycle (endless loop)
        while(slow != null) {
            temp = slow.next;
            slow.next = prev;
            // move to next nodes
            prev = slow;
            slow = temp;
        }

        // slow is at the end (null), reset fast, compare slow and fast
        fast = head;
        slow = prev; // (prev points to the last node, slow is null)
        while(slow != null) {
            if(fast.val != slow.val) return false;
            fast = fast.next;
            slow = slow.next;
        }
        return true;
    }
}