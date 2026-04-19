"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def get_all_same_value(coords, n):
            val = grid[coords[1]][coords[0]]
            for i in range(n):
                for j in range(n):
                    if val != grid[coords[1] + i][coords[0] + j]:
                        return False
            return True

        n = len(grid)
        def get_quad_tree(coords, n):
            mid =  n // 2
            if n == 0:
                return None
            root = Node(grid[coords[1]][coords[0]], True, None,None,None,None)

            if get_all_same_value(coords, n):
                return root
            root.isLeaf = False
            root.topLeft = get_quad_tree(coords, mid)
            root.topRight = get_quad_tree((coords[0] + mid, coords[1]), mid)
            root.bottomLeft = get_quad_tree((coords[0], coords[1] + mid), mid)
            root.bottomRight = get_quad_tree((coords[0] + mid, coords[1] + mid), mid)
            return root
        return get_quad_tree((0,0), n)

