class Solution(object):
    def minSubArrayLen(self, s, nums):
        _ = []
        result = []
        for i in range(len(nums)):
            _.append(self.helper(nums[i:],s,[]))
            result = []
        for numbers in _:
            if numbers != None:
                result.append(len(numbers))
        return min(result) if len(result) != 0 else 0

    def helper(self,nums,target,res):
        if target==0:
            return res

        if len(nums) != 0:
            res.append(nums[0])
            return self.helper(nums[1:],target-nums[0],res)



a = Solution()
print(a.minSubArrayLen(11,[1,2,3,4,5]))


# [2,3,1,2,4,3] n=7
# [4,3] ouput = 2