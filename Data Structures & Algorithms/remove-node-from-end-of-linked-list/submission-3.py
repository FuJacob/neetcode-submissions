# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        length = 0
        dummy = head
        while dummy:
            length+=1
            dummy = dummy.next
        ## 3 . so 3- 2 = 1. + 1 = 2 
        ## ok 
        target_from_start = length - n + 1

        if target_from_start == 1:
            return head.next

        count = 1
        prev = None
        curr = head
        while curr and count != target_from_start:
            prev = curr
            curr = curr.next
            count+=1
        
        prev.next = curr.next



        return head