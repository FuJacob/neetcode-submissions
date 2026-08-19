# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ans = dummy
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = carry + v1 + v2
            carry = total // 10
            curr = ListNode(total % 10)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
            dummy.next = curr
            dummy = dummy.next
            
        if carry != 0:
            dummy.next = ListNode(carry)
        return ans.next
        


            


