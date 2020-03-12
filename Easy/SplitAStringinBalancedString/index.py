class Solution(object):
    def balancedStringSplit(self, s):
        temp = 0
        result = 0
        for i in range(len(s)):
            if s[i] == "R":
                temp += 1
            else:
                temp += -1


            if temp == 0:
                result += 1

        return result




a = Solution()
print(a.balancedStringSplit("RLRRLLRLRL"))