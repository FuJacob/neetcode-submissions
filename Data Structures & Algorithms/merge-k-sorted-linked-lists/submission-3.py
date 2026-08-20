# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val,i, l.next))
        curr = dummy = ListNode()
        while heap:
            val,idx, nxt = heapq.heappop(heap)
            dummy.next = ListNode(val)
            dummy = dummy.next
            if nxt:
                heapq.heappush(heap, (nxt.val,idx, nxt.next))
        return curr.next
