class Solution(object):
    def subtractProductAndSum(self, n):
        num = str(n)
        product = 1
        sum = 0
        for i in range(len(num)):
            product *= int(num[i])
            sum += int(num[i])

        return product - sum







a = Solution()
print(a.subtractProductAndSum(234))