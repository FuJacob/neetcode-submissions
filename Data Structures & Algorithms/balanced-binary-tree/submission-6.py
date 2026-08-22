# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def treeHeight(root):
            nonlocal ans
            if not root or not ans:
                return 0
            left, right = treeHeight(root.left), treeHeight(root.right)
            if abs(right - left) > 1:
                ans = False
            return max(right,left) + 1
        treeHeight(root)
        return ans

                
