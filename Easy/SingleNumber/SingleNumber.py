class Solution(object):
    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i - 1]:
                return nums[i - 1]
        return nums[-1]




a = Solution()
