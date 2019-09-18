#递归
# class Solution(object):
#     def climbStairs(self, n):
#         if n == 1:
#             return 1
#         elif n ==2:
#             return 2
#         else:
#             return self.climbStairs(n-1) + self.climbStairs(n-2)

#DP
class Solution(object):
    def climbStairs(self, n):
        if n<3:
            return n
        c1 = 1
        c2 = 2
        for i in range(3,n+1):
            holder = c1 + c2
            c1 = c2
            c2 = holder
        return c2