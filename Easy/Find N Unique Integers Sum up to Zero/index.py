class Solution(object):
    def sumZero(self, n):
        if n %2 == 1:
            return [i for i in range(-n // 2 + 1, n // 2 + 1)]
        else:
            res = []
            for i in range(-n//2,n//2+1):
                if i !=0:
                    res.append(i)
            return res
a = Solution()
print(a.sumZero(4))