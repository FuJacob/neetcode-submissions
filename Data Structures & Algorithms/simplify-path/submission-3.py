class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split('/')
        stack = []
        for t in tokens:
            if t == '..':
                if stack:
                    stack.pop()
                continue
            if t and t != '.' and t[0] != '/':
                stack.append(t)
        res = "/" + "/".join(stack)
        return res

            
