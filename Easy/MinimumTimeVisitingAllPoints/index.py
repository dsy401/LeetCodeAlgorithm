class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        x, y = points[0][0], points[0][1]
        nm = 0
        for i in points[1:]:
            nm += max(abs(x - i[0]), abs(y - i[1]))
            x, y = i[0], i[1]
        return nm





a = Solution()
print(a.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))