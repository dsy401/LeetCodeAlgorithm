class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n ==0:
            return round(1,5)
        elif n >0:
            result = x
            for i in range(n - 1):
                result = result * x
            return round(result,5)
        else:
            result = x
            n = n * -1
            for i in range(n - 1):
                result = result * x
            return round(1/result,5)

