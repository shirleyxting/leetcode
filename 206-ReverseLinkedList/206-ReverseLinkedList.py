# Last updated: 6/28/2026, 9:06:33 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head:
9            return head
10        prev = head
11        curr = head.next
12        prev.next = None
13        while curr:
14            temp = curr.next
15            curr.next = prev
16            prev = curr
17            curr = temp
18        return prev