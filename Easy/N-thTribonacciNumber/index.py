class Solution(object):
    def tribonacci(self, n):
        first = 0
        second = 1
        third = 1

        if n ==0:
            return first
        elif n ==1:
            return second
        elif n ==2:
            return third
        else:
            for i in range(2, n):
                temp_1 = first
                temp_2 = second
                temp_3 = third

                first = temp_2
                second = temp_3
                third = temp_1 + temp_2 + temp_3

            return third




a = Solution()
print(a.tribonacci(25))