
class Solution(object):
    def removeOuterParentheses(self, S):
        stack = []
        res = ""
        temp = ""
        for i in range(len(S)):
            temp += S[i]
            if S[i] == "(":
                stack.append(S[i])
            else:
                stack.pop()


            if len(stack) == 0:
                res += temp[1:-1]
                temp = ''
        return res


a = Solution()
print(a.removeOuterParentheses("(()())(())"))