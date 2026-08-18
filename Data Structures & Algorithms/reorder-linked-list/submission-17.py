# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        ## slow is at the mid point
        second = slow.next ## thje one ater miod
        slow.next = None
        ptr1, ptr2 = head, reverse(second)
        while ptr1 and ptr2:
            nxt1, nxt2 = ptr1.next, ptr2.next
            ptr1.next = ptr2
            ptr2.next = nxt1
            ptr1 = nxt1
            ptr2 = nxt2
