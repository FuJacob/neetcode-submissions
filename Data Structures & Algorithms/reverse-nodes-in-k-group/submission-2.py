# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev = dummy
        while True:
            kth = groupPrev ## start here
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next ## ans cuzno more
                ## this wil lget us the kth node
            groupNxt = kth.next
            prev = groupNxt ## want to connet aff group next
            curr = groupPrev.next
            while curr != groupNxt:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            ## reconnect
            oldGroupHead = groupPrev.next
            groupPrev.next = kth
            groupPrev = oldGroupHead
        return dummy.next