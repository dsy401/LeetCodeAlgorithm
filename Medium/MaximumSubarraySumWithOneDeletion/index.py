class Solution(object):
    def maximumSum(self, arr):
        if len(arr) == 1:
            return max(self.sub_max_arr(arr))
        else:
            deleted_sum_arr = []
            for i in range(len(arr)):
                new_array = arr[0:]
                new_array.pop(i)
                deleted_sum_arr.append(sum(new_array))

            max_value = max(self.sub_max_arr(arr))

            if max_value > max(deleted_sum_arr):
                return max_value
            else:
                return max(deleted_sum_arr)

    def sub_max_arr(self,arr):
        sublist = []

        # first loop
        for i in range(len(arr) + 1):

            # second loop
            for j in range(i + 1, len(arr) + 1):
                # slice the subarray
                sub = arr[i:j]
                sublist.append(sum(sub))
        return sublist



a = Solution()
print((a.maximumSum([1,-4,-5,-2,5,0,-1,2])))
# expected 3
