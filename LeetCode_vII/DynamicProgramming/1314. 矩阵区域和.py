## written by xiongbiao
## date 2020-6-5

'''
给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 
i - K <= r <= i + K, j - K <= c <= j + K 
(r, c) 在矩阵内。
'''


class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] += dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1] + mat[i-1][j-1]


        def get(x, y):
            x = max(min(m, x), 0)
            y = max(min(n, y), 0)
            return dp[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + K + 1, j + K + 1) - get(i - K, j + K + 1) - get(i + K + 1, j - K) + get(i - K, j - K)
        return ans
