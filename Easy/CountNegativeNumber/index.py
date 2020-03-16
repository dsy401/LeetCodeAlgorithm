class Solution(object):
    def countNegatives(self, grid):
        sum = 0
        for row in grid:
            for col in row:
                if col <0:
                    sum+=1

        return sum



a = Solution()
print(a.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))