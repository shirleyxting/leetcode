// Last updated: 8/16/2026, 9:49:11 PM
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
    // public ListNode middleNode(ListNode head) {
    //     // return the n/2+1 node, n is the length of ListNode
    //     if(head == null) return head;
    //     ListNode curr = head;
    //     int n = 0;
    //     while(curr != null) {
    //         n ++;
    //         curr = curr.next;
    //     }
    //     curr = head;
    //     for(int i = 1; i < n/2+1; i ++) {
    //         curr = curr.next;
    //     }
    //     return curr;
    // }

    // method 2 - slow and fast pointers
    // slow moves 1 step, fast moves 2 steps, 
    // when fast arrives the end, slow is at the middle
    public ListNode middleNode(ListNode head) {
        if(head == null) return head;
        ListNode fast = head, slow = head;
        while(fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }
}