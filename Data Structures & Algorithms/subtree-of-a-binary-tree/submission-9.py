# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        target = None
        ans = False
        def treeHash(root, searching):
            nonlocal target, ans
            if not root:
                return "#"
            left_hash = treeHash(root.left, searching)
            right_hash = treeHash(root.right, searching)
            root_hash = hash((root.val, left_hash, right_hash))
            if root_hash == target and searching:
                ans = True
            return root_hash

        target = treeHash(subRoot, False)
        treeHash(root, True)
        return ans
