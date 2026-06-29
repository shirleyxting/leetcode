# Last updated: 6/28/2026, 9:21:18 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        # if not head:
9        #     return head
10        # prev = head
11        # curr = head.next
12        # prev.next = None
13        # while curr:
14        #     temp = curr.next
15        #     curr.next = prev
16        #     prev = curr
17        #     curr = temp
18        # return prev
19    
20        #  iterate nodes, and set each node's next to prev
21        prev = None
22        curr = head
23
24        while curr:
25            # change curr.next to prev
26            temp = curr.next
27            curr.next = prev
28            
29            # update prev to curr
30            prev = curr
31            # move next step, update curr to curr.next (temp)
32            curr = temp
33        
34        # curr is None, prev is the head
35        return prev
36