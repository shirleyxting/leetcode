# Last updated: 9/30/2026, 5:52:26 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
8        # get length 'n' and tail (for later connecting with head)
9        # k = k % n
10        # new_tail = (n-k) node
11        # new_head = new_tail.next
12        # then connect tail with head
13
14        if not head or not head.next:
15            # empty or signle node
16            return head
17        
18        tail = head
19        n = 1
20        while tail.next:
21            n += 1
22            tail = tail.next
23        
24        k %= n
25        if k == 0:
26            return head
27            
28        new_tail = head
29        for _ in range(n-k-1):
30            new_tail = new_tail.next
31        
32        new_head = new_tail.next
33
34        # connect tail with head
35        new_tail.next = None
36        tail.next = head
37
38        return new_head
39