import math
class Solution(object):
    def majorityElement(self, nums):

        if len(nums) == 0:
            return 0

        pos = math.floor(len(nums)/2)


        c = 0
        for num in nums:
            if num > pos:
                c +=1

        return c



a = Solution()

print(a.majorityElement([2,2,1,1,1,2,2]))