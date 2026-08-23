# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ## singel ptr for preorder we can do eac hone by one 
        preorder_ptr = 0
        m,n = len(preorder), len(inorder)
        inorder_val_to_idx = {}
        for i,v in enumerate(inorder):
            inorder_val_to_idx[v] = i
        def dfs(left,right):
            nonlocal preorder_ptr
            if left > right or preorder_ptr >= m:
                return None
            root = TreeNode(preorder[preorder_ptr]) ## ? 
            preorder_ptr+=1
            inorder_idx = inorder_val_to_idx[root.val]
            root.left = dfs(left, inorder_idx - 1)
            root.right = dfs(inorder_idx + 1, right)
            return root
        return dfs(0, n - 1)
