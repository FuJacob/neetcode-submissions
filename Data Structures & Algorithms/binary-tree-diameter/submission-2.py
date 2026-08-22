# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def treeDepth(root):
            nonlocal ans
            if not root:
                return 0
            left = right = 0
            if root.left:
                left = treeDepth(root.left) + 1
            if root.right:
                right = treeDepth(root.right) + 1
            ans = max(ans, left+right)
            return max(left,right)
        treeDepth(root)
        return ans