class Solution(object):
    def maximum69Number(self, num):
        arr = [num]

        num = str(num)

        for i in range(len(num)):
            if num[i] == "6":
                arr.append(int(num[:i] + "9" + num[i+1:]))
            else:
                arr.append(int(num[:i] + "6" + num[i + 1:]))
        return max(arr)

a = Solution()
print(a.maximum69Number(9669))