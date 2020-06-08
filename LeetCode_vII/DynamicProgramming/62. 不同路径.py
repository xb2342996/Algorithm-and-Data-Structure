## written by xiongbiao
## date 2020-6-7
'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
'''
class Solution(object):
    '''
    时间复杂度O（n^2) 空间复杂度O（min(m,n))
    '''
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < n:
            m, n = n, m
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]

        return dp[-1]
    '''
    时间复杂度O（n^2) 空间复杂度O（n^2)
    '''
    # def uniquePaths(self, m, n):
    #     """
    #     :type m: int
    #     :type n: int
    #     :rtype: int
    #     """
    #     dp = [[0] * n for _ in range(m)]
    #     for i in range(n):
    #         dp[0][i] = 1
    #     for i in range(m):
    #         dp[i][0] = 1
    #
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[i][j] = dp[i-1][j] +dp[i][j-1]
    #
    #     return dp[-1][-1]