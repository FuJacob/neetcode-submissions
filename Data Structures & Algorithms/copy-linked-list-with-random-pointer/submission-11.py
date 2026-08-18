"""
# Definition for a Node.
class Node:
def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = head 
        while dummy:
            copy = Node(dummy.val)
            nxt = dummy.next
            dummy.next = copy
            copy.next = nxt
            dummy = nxt
            ## this loop makes copy, places it next, interleavesi t baiscally
        
        ## then we need to get answer? 
        dummy = head ## ohh set random first cuz next starts unweaving it whic hisnt good.
        while dummy:
            copy = dummy.next
            if dummy.random:
                copy_random = dummy.random.next
                copy.random = copy_random
            dummy = dummy.next.next
        
        dummy = head
        ans = dummy.next if dummy else None
        while dummy:
            copy = dummy.next
            dummy_nxt = copy.next
            if dummy_nxt:
                copy.next = dummy_nxt.next
            dummy.next = dummy_nxt
            dummy = dummy.next
        
        return ans