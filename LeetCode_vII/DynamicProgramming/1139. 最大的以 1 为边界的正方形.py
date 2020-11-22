# written by xiongbiao
# date 2020-11-22

'''
给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回 0。
'''

class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])
        dp = [[[0] * 2 for _ in range(column + 1)] for _ in range(row + 1)]

        for i in range(1, row + 1):
            for j in range(1, column + 1):
                if grid[i - 1][j - 1] == 1:
                    dp[i][j][0] = 1 + dp[i][j-1][0] # 行
                    dp[i][j][1] = 1 + dp[i-1][j][1] # 列
        res = 0
        for i in range(1, row + 1):
            for j in range(1, column + 1):
                side = min(dp[i][j][0], dp[i][j][1])
                for k in range(side + 1, 0, -1):
                    if dp[i - k + 1][j][0] >= k and dp[i][j - k + 1][1] >= k:
                        res = max(res, k)
                        break
        return res * res

print(Solution().largest1BorderedSquare([[1,1,1],[1,0,1],[1,1,1]]))