class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = [] ## hold nums
        str_stack = [] ## hold completed bits
        curr_num = 0 ## currnum
        curr_str = '' ## curr str
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c) ## bild on curr num
            elif c == '[': ## start? add chunk 
                str_stack.append(curr_str) ## add watever we have so far
                num_stack.append(curr_num) ## add wnatever nium we ahve so far
                curr_num = 0 ## reste
                curr_str = ''# #reset
            elif c == ']': ## done?
                repeat = num_stack.pop() #3 repeat how many
                prev = str_stack.pop() ## what oru string before
                curr_str = prev + repeat * curr_str ##repeat curr str ## tjs is or new curr str
            else:
                curr_str +=c
        return curr_str
                


