class Solution(object):
    def generateTheString(self, n):

        if n ==2:
            return "xy"

        if n %2 ==0:
            s = "x"*(n//2-1) + "y"*(n//2+1)
        if n%2 ==1:
            s = "x"*(n//2+1) + "y"*(n//2)

        return s



a = Solution()
print(a.generateTheString(2))