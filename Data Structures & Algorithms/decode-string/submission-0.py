class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        stack = []
        curr_num = 0
        for c in s:
            if '0' <= c <= '9':
                curr_num = curr_num * 10 + int(c)
                continue
            if c == '[':
                nums.append(curr_num)
                curr_num = 0
            if c == ']':
                curr = ''
                while stack and stack[-1] != '[':
                    curr = stack[-1] + curr
                    stack.pop()
                if stack:
                    stack.pop()
                stack.append(nums.pop() * curr)
                continue
            stack.append(c)
        return "".join(stack)
                


