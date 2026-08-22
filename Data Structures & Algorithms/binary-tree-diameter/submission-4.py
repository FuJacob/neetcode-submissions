# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def treeDepth(root): ## returns maximum depth of entire tree not diatmer
            nonlocal ans
            if not root:
                return 0
            left = treeDepth(root.left)
            right = treeDepth(root.right)
            ans = max(ans, left+right)
            return max(left,right) + 1
        treeDepth(root)
        return ans