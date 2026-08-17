# Last updated: 8/16/2026, 9:52:04 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if not head or not head.next: return False

        # visited = []
        # pos = 0

        # curr = head
        # while curr.next:
        #     if curr not in visited:
        #         visited.append(curr)
        #         curr = curr.next
        #         pos += 1
        #     else:
        #         return True
        
        # return False

        # two pointers, hare and tortoise
        # if there is a cycle, slow will catch fast eventually
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True

        return False
        
