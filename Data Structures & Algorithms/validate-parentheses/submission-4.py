class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {'(':')', '[':']', '{':'}'}
        stack = []
        for c in s:
            if c in open_to_close:
                stack.append(c)
            else:
                if not stack or c != open_to_close[stack[-1]]:
                    return False
                stack.pop()
        return len(stack) == 0
