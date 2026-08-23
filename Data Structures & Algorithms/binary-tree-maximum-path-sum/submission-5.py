# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(root): # clacuate on the fly max path sm, calcuating as if each node is th connecting one 
            nonlocal ans
            if not root:
                return 0
            left_max_path_sum = max(0, dfs(root.left))
            right_max_path_sum = max(0,dfs(root.right))
            ans = max(ans, root.val + left_max_path_sum + right_max_path_sum)
            return max(left_max_path_sum, right_max_path_sum) + root.val
        dfs(root)
        return ans