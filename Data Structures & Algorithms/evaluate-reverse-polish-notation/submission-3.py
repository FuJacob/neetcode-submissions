class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ## given an array of strings tokens that represent a valid arithmetic expression
        ## in reverse polish notation

        """
        return an integer that represents the evaluation of it

        i think we could have a stack that carries the numbers
        push each num in, once we hit cuz it's valid operations
        so once we hit an op, we pop the last 2 numbers off and create teh number
        then just push that result into our stack
        then continue on

        """
        stack = []
        ops = set(['+', '-', '*', '/'])
        for t in tokens:
            if t in ops:
                second,first = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(first+second)
                elif t == '-':
                    stack.append(first-second)
                elif t == '*':
                    stack.append(first*second)
                else:
                    stack.append(int(first/second))
            #3 if it's not op w ejust push it in the stack
            else:
                stack.append(int(t))
        ## then afterwards we should end up with just one number
        return stack[0]