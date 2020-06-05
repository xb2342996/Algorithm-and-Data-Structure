## written by xiongbiao
## date 2020-6-5

'''
给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。
'''
class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        cols, rows = len(matrix[0]), len(matrix)
        print(cols)
        dp = [[0] * cols for _ in range(rows)]

        ans = 0
        for m in range(rows):
            for n in range(cols):
                if matrix[m][n] == 0:
                    dp[m][n] = 0
                elif m == 0 or n == 0:
                    dp[m][n] = matrix[m][n]
                else:
                    dp[m][n] = min(dp[m][n-1], dp[m-1][n], dp[m-1][n-1]) + 1
                ans += dp[m][n]
        return ans


Solution().countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]])

