// Last updated: 8/16/2026, 9:53:35 PM
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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // // iterative approach
        // if(list1 == null) return list2;
        // if(list2 == null) return list1;

        // ListNode res = new ListNode();
        // ListNode dummy = new ListNode();
        // res = dummy;

        // while(list1 != null && list2 != null) {
        //     if(list1.val < list2.val) {
        //         dummy.next = list1;
        //         list1 = list1.next;
        //     } else {
        //         dummy.next = list2;
        //         list2 = list2.next;
        //     }
        //     dummy = dummy.next;
        // }
        // if(list1 != null) dummy.next = list1;
        // if(list2 != null) dummy.next = list2;
        // return res.next;

        // recursive approach
        if(list1 == null) return list2;
        if(list2 == null) return list1;

        if (list1.val < list2.val) {
            list1.next = mergeTwoLists(list1.next, list2);
            return list1;
        } else {
            list2.next = mergeTwoLists(list1, list2.next);
            return list2;
        }
    }
}