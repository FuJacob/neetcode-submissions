# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0
        for l in lists:
            if not l:
                continue
            heapq.heappush(heap, (l.val,count, l))
            count+=1
        ans = None
        dummy = None
        while heap:
            val,c, l = heapq.heappop(heap)
            if ans:
                ans.next = l
                ans = ans.next
            else:
                dummy = l
                ans = l
            if l.next:
                heapq.heappush(heap, (l.next.val,c, l.next))
        return dummy
            

