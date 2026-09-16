# Last updated: 9/16/2026, 3:20:21 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
8        if head is None:
9            return None
10
11        dummy = ListNode(0, head)
12        # starts from dummy, instead of head (to deal with "deleting head node" situation)
13        slow, fast = dummy, dummy
14
15        # fast go (n+1) steps, then slow starts
16        # when fast = None (reach the end), slow stops at "3" (prev node of the deleting one)
17        for _ in range(n + 1):
18            fast = fast.next
19        
20        while fast:
21            fast = fast.next
22            slow = slow.next
23        
24        slow.next = slow.next.next
25
26        return dummy.next
27            