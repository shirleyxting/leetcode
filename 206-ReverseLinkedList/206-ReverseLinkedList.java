// Last updated: 8/16/2026, 9:51:26 PM
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
    // public ListNode reverseList(ListNode head) {
    //     ListNode newHead = null; 

    //     while(head != null) {
    //         ListNode next = head.next; // next=2
    //         head.next = newHead; // set 1->null (newHead)
            
    //         newHead = head; // update newHead to head = 1
    //         head = next; // move to next node, from 1 to 2
    //     }
    //     return newHead;
    // }

    // method 2 - recursion - Traversal
    // recursion = {Traversal [top-down], Divide and Conquer [bottom-up]}
    public ListNode reverseList(ListNode head) {
        return helper(head, null);
        // return reversed Listnode with newHead=null
    }

    private ListNode helper(ListNode head, ListNode newHead) {
        // return reversed ListNode with head replaced to newHead
        if(head == null) return newHead; //recursion exit

        ListNode next = head.next;
        head.next = newHead;

        return helper(next, head);

    }
}