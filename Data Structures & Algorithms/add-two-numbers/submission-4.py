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
            curr = ListNode()
            if not l1:
                ## l2 exists
                total = (carry + l2.val)
                curr.val = total % 10
                carry = total // 10
                l2 = l2.next
            elif not l2:
                total = (carry + l1.val)
                curr.val = total % 10
                carry = total // 10
                l1 = l1.next
            else:
                total = carry + l1.val + l2.val
                curr.val = total % 10
                carry = total // 10
                l1 = l1.next
                l2 = l2.next
            dummy.next = curr
            dummy = dummy.next
        if carry != 0:
            dummy.next = ListNode(carry)
        return ans.next
        


            


