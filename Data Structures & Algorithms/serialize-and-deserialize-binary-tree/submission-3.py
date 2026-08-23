# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tokens = []
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                tokens.append("#")
            else:
                tokens.append(str(curr.val))
                stack.append(curr.right)
                stack.append(curr.left)
        return ",".join(tokens)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ## preorder? middle left right i thin kwe can do this wiht a ptr then
        dummy = TreeNode()
        n = len(data)
        preorder_ptr = 0
        def dfs():
            nonlocal preorder_ptr
            if preorder_ptr >= n:
                return None
            start = preorder_ptr
            while data[preorder_ptr] not in [",", "#"]:
                preorder_ptr +=1
            if start == preorder_ptr:
                val = None
            else:
                val = int(data[start:preorder_ptr])
            root = TreeNode(val)
            root.left = dfs()
            root.right = dfs()
            preorder_ptr+=1
            return root
        return root
                



