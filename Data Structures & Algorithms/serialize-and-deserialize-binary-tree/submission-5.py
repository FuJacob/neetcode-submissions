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
        dummy = TreeNode()
        tokens = data.split(",")
        n = len(tokens)
        ptr = 0
        def dfs():
            nonlocal ptr
            if ptr >= n:
                return None
            if tokens[ptr] == "#":
                ptr+=1
                return None
            node = TreeNode(int(tokens[ptr]))
            ptr+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
