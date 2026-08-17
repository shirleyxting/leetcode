// Last updated: 8/16/2026, 9:52:08 PM
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    // public boolean hasCycle(ListNode head) {
    //     if(head == null) return false;
    //     Set<ListNode> visited = new HashSet<>();
    //     ListNode curr = head;
        
    //     while(curr != null) {
    //         if (visited.contains(curr)) {
    //             return true;
    //         } else {
    //             visited.add(curr);
    //         }
    //         curr = curr.next;
    //     }
    //     return false;
    // }

    // method 2 - two pointers, hare and tortoise
    // fast pointer moves 2 steps at a time. 
    // slow               1
    // if there is a cycle, slow will catch up the fast eventually
    public boolean hasCycle(ListNode head) {
        ListNode fast = head, slow = head;
        while(fast != null && fast.next != null && slow != null) {
            fast = fast.next.next;
            slow = slow.next;
            if(fast == slow) return true;
        }
        return false;
    }
}