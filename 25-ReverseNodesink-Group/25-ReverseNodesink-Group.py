# Last updated: 8/20/2026, 8:32:15 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        # 2->1, 1: head, head.next = 4 (next reverseK return)
9        # 4->3, 3: head, head.next = 5 (next reverseK return)
10        # 5,    5: head, head.next = None
11
12        # check if we have enough K nodes, starting from head
13        node = head
14        count = 0
15        while node and count < k:
16            count += 1
17            node = node.next
18        if count < k:
19            return head  # less than k, no operation
20        
21        # reverse K nodes
22        prev = None
23        curr = head
24        for _ in range(k):
25            temp = curr.next
26            curr.next = prev
27            prev = curr
28            curr = temp
29        
30        # head: the tail after reverse
31        # prev: new head after reverse
32        # curr: the start node of remaining linked list
33
34        head.next = self.reverseKGroup(curr, k)
35        # link current-k-reversed part with next-k-reversed part's head
36
37        return prev  # return the new head