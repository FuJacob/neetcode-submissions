# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans, k
            if not root:
                return
            dfs(root.left)
            if k == 1:
                ans = root.val
            k -= 1
            dfs(root.right)
        dfs(root)
        return ans