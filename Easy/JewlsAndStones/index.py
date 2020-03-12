class Solution(object):
    def numJewelsInStones(self, J, S):
        result = 0
        S = list(S)
        for c in S:
            if c in J:
                result+=1
        return result


a = Solution()
print(a.numJewelsInStones("aA","aAAbbbb"))