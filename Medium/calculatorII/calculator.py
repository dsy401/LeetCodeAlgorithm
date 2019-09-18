class Solution(object):
    def calculate(self, s):

        num, preOp, stack = 0, '+', []
        for i, e in enumerate(s):
            if e.isdigit():
                num = num * 10 + int(e)
            if e in '+-*/' or i == len(s)-1:
                if preOp == '+':
                    stack += [num]
                elif preOp == '-':
                    stack += [-num]
                elif preOp == '*':
                    stack += [stack.pop() * num]
                else:
                    stack += [int(stack.pop() / num)]
                preOp = e
                num = 0
        return sum(stack)