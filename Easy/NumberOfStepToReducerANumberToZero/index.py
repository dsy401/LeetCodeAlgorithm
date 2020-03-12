class Solution(object):
    def numberOfSteps(self, num):
        return self.helper(num,0)


    def helper(self,num,count):
        if num == 0:
            return count
        else:
            if num % 2 == 1:
                num = num -1
                return self.helper(num,count+1)
            else:
                num  = num /2
                return self.helper(num,count+1)




a = Solution()
print(a.numberOfSteps(123))