# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        stack = [(root,root.val)]
        while stack:
            top, greatest = stack.pop()
            if top.val >= greatest:
                ans+=1
            new_greatest = max(greatest, top.val)
            if top.left:
                stack.append((top.left, new_greatest))
            if top.right:
                stack.append((top.right, new_greatest))
        return ans
