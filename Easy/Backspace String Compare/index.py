class Solution(object):
    def backspaceCompare(self, S, T):
        s_stack =[]
        t_stack = []
        for word in S:
            if word == "#":
                if len(s_stack) !=0:
                    s_stack.pop()
            else:
                s_stack.append(word)

        for word in T:
            if word == "#":
                if len(t_stack) !=0:
                    t_stack.pop()
            else:
                t_stack.append(word)

        return s_stack == t_stack


a = Solution()
print(a.backspaceCompare("ab######c","ad#c"))