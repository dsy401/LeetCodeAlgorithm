class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        new_dict = {}
        for num in arr:
            if num in new_dict:
                new_dict[num] += 1
            else:
                new_dict[num] = 1
        for key in new_dict:
            if (new_dict[key]/len(arr)):
                count+= new_dict[key]
        return count


a = Solution()
print(a.findSpecialInteger([1,2,2,6,6,6,6,7,10]))