# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        first_iteration = True
        ans = head
        prev_tail = None
        while head:
            new_tail = head
            while head and count != k:
                count+=1
                if count != k:
                    head = head.next
            if not head:
                break
            new_head = head
            head = head.next
            if first_iteration:
                ans = new_head
                first_iteration = False

            if prev_tail:
                prev_tail.next = new_head
            prev = head
            ## start iwth node after group
            curr = new_tail
            while curr != head:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            prev_tail = new_tail
            count = 0
            
        return ans