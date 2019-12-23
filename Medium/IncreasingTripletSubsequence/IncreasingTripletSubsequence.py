class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        currMin = nums[0]
        currSecond = float('inf')
        for i in range(1,len(nums)):
            if nums[i] <= currMin:
                currMin = nums[i]
            elif nums[i] < currSecond:
                currSecond = nums[i]
            if nums[i] > currSecond:
                return True
        return False

a = Solution()
print(a.increasingTriplet([1, 2, 3, 4, 5]))