# Last updated: 8/16/2026, 9:49:08 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or not head.next: return head

        # len = 0
        # node = head
        # while node:
        #     len += 1
        #     node = node.next
        
        # middle_idx = len // 2

        # while middle_idx > 0:
        #     middle_idx -= 1
        #     head = head.next
        
        # return head

        # method 2 - slow and fast pointers
        # slow moves 1 step, fast moves 2 steps, 
        # when fast arrives the end, slow is at the middle
        if not head or not head.next: return head

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow