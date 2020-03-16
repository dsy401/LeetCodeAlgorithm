class Solution(object):
    def findLengthOfLCIS(self, nums):
        if nums ==[]:
            return 0

        arr = []
        temp = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                temp +=1
            else:
                arr.append(temp)
                temp = 1

        if len(arr) == 0:
            return temp
        else:
            return max(max(arr),temp)



a = Solution()
print(a.findLengthOfLCIS([1,3,5,4,7]))