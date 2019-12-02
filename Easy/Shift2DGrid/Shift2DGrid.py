class Solution(object):
    def shiftGrid(self, grid, k):
        row = len(grid)
        col = len(grid[0])
        res = [[0 for x in range(col)] for y in range(row)]
        total = row * col
        start = total - k % total
        for i in range(row):
            for j in range(col):
                num = (start + col * i + j) % total
                res[i][j] = grid[num//col][num%col]
        return res




