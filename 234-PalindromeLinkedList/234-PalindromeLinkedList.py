# Last updated: 8/16/2026, 9:51:00 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # converted_list = []
        # while head:
        #     converted_list.append(head.val)
        #     head = head.next
        
        # l = 0
        # r = len(converted_list) - 1
        # while l <= r:
        #     if converted_list[l] != converted_list[r]:
        #         return False
        #     l += 1
        #     r -= 1
        
        # return True  

        # method-2: reverse the second half of the linked list, and then compare
        # Floyd's Cycle to find the middle point
        # when fast reades end (fast == null || fast.next == null), slow is at MIDDLE

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is the middle point, reverse it
        reverse = self.reverse(slow)

        while reverse:
            if reverse.val != head.val: return False
            reverse = reverse.next
            head = head.next
        
        return True


    # reverse linked list starting with 'head'
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


