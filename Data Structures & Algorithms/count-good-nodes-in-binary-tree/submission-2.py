# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def findGoodNodes(root, greatest):
            nonlocal ans
            if not root:
                return
            if root.val >= greatest:
                ans+=1
            new_greatest = max(greatest, root.val)
            findGoodNodes(root.left, new_greatest)
            findGoodNodes(root.right, new_greatest)
        
        findGoodNodes(root, float('-inf'))
        return ans
