class Solution:
    def permute(self, nums):
        res = []
        if len(nums) == []:
            return [[]]
        elif len(nums) == 1:
            return [nums]
        elif len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        else:
            for i in range(len(nums)):
              res = res + (self.zipp(nums[i], self.permute(nums[:i]+nums[i+1:])))
              print(res)
            return res

    def zipp(self, a, b):
        ress = []
        for i in range(len(b)):
            ress.append([a] + b[i])
        return ress


a = Solution()
print(a.permute([1,2,3]))