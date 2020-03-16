class Solution(object):
    def replaceElements(self, arr):
        for i in range(len(arr)):
            sub_arr = arr[i+1:]
            arr[i] = max(sub_arr) if len(sub_arr) !=0 else -1
        return arr





a = Solution()
print(a.replaceElements([17,18,5,4,6,1]))