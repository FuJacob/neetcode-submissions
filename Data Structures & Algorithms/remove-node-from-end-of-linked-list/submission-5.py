# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(n+1):
            fast = fast.next ## we do n+ 1 so gap is n+1 nodes, this by time fast dies, slow is on nodeb4 delete
            ## and we do dummy node why? so then we dont need to dela with edgecase?
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next