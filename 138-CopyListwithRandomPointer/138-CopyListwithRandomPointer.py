# Last updated: 9/16/2026, 4:47:34 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        # randome can point to nodes we havn't created yet
13        # so we have to scan original linked list twice
14        # 1: build old->new hashmap, and create new Nods
15        # 2: setup next and random pointers for NEW
16
17        old_to_new = {None: None}
18        
19        curr = head
20        while curr:
21            old_to_new[curr] = Node(curr.val)
22            curr = curr.next
23        
24        curr = head
25        while curr:
26            old_to_new[curr].next = old_to_new[curr.next]
27            old_to_new[curr].random = old_to_new[curr.random]
28            curr = curr.next
29        
30        return old_to_new[head]