"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


given node in conenected undierctye graph
return deepcopy of graph

"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        root = Node(node.val)

        visited = {node: root} ## map og to new node
        q = deque([(node,root)])
        while q:
            og_node, new_node = q.popleft()
            for nei in og_node.neighbors:
                if nei not in visited: 
                    new_nei = Node(nei.val)
                    visited[nei] = new_nei
                    q.append((nei, new_nei))
                new_node.neighbors.append(visited[nei])

        return root








