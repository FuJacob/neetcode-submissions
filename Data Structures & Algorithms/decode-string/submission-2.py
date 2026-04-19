class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        curr_num = 0
        curr_str = ''
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[': ## add chunk
                str_stack.append(curr_str)
                num_stack.append(curr_num)
                curr_num = 0
                curr_str = ''
            elif c == ']':
                repeat = num_stack.pop()
                prev = str_stack.pop()
                curr_str = prev + repeat * curr_str
            else:
                curr_str +=c
        return curr_str
                


