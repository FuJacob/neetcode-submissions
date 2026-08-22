# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        found = False
        target = None
        def tree_hash(root, looking):
            nonlocal target, found
            if not root:
                return "#"
            left_hash = tree_hash(root.left, looking)
            right_hash = tree_hash(root.right, looking)
            
            root_hash = str(root.val) + "#" + left_hash + right_hash

            if looking and root_hash == target:
                found = True
            return root_hash
        target = tree_hash(subRoot, False)
        tree_hash(root, True)
        return found
            
        

