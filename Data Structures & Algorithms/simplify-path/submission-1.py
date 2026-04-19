class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split('/')
        stack = []
        for t in tokens:
            if not t or t == '.' or t[0] == '/':
                continue
            if t == '..':
                if stack:
                    stack.pop()
                continue
            stack.append(t)
        res = "/".join(stack)
        res = "/" + res
        return res

            
