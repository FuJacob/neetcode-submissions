# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(root):
            nonlocal ans
            if not root:
                return float('-inf')
            left_max_path_sum = dfs(root.left)
            right_max_path_sum = dfs(root.right)
            ans = max(ans, left_max_path_sum, right_max_path_sum, root.val + left_max_path_sum,root.val + right_max_path_sum, left_max_path_sum + right_max_path_sum + root.val, root.val)
            return max(0, left_max_path_sum, right_max_path_sum) + root.val
        dfs(root)
        return ans