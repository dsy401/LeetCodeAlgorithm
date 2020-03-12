class Solution(object):
    def decompressRLElist(self, nums):
        result = []
        for i in range(0,len(nums)-1,2):
            freq = nums[i]
            val = nums[i+1]
            sub_result = freq*[val]
            result += sub_result
        return result
a= Solution()
print(a.decompressRLElist([1,2,3,4]))