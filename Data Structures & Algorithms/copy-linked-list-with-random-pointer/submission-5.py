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
        """
map each node to a clone of itself 

iterate thru
then iterate tio fill in random by comapring aaccoridngly . 
        """
        dummy = head
        og_to_copy = {}
        while dummy:
            og_to_copy[dummy] = Node(dummy.val)
            dummy = dummy.next
        dummy2 = head
        while dummy2:
            if dummy2.next:
                og_to_copy[dummy2].next = og_to_copy[dummy2.next]
            if dummy2.random:
                og_to_copy[dummy2].random = og_to_copy[dummy2.random]
            dummy2 = dummy2.next
        return og_to_copy[head] if head else None
