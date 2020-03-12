class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count +=1
            result.append(count)

        return result




a = Solution()
print(a.smallerNumbersThanCurrent([7,7,7,7,7]))