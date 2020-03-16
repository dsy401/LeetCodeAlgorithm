class Solution(object):
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and arr[j]*2 == arr[i]:
                    return True

        return False

a = Solution()
print(a.checkIfExist([3,1,7,11]))