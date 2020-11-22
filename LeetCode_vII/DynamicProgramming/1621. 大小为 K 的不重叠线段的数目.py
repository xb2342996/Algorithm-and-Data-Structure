# written by xiongbiao
# date 2020-11-21

'''
给你一维空间的 n 个点，其中第 i 个点（编号从 0 到 n-1）位于 x = i 处，请你找到 恰好 k 个不重叠 线段且每个线段至少覆盖两个点的方案数。线段的两个端点必须都是 整数坐标 。这 k 个线段不需要全部覆盖全部 n 个点，且它们的端点 可以 重合。
请你返回 k 个不重叠线段的方案数。由于答案可能很大，请将结果对 109 + 7 取余 后返回。
'''

class Solution(object):
    '''
    dp[i][j][k] i表示第几个点，j表示第几条线段，k表示线段右端点是不是这在i上
     dp[i][j][0]表示第j条线段的右端不是i
     dp[i][j][1]表示第j条线段的右端是i
     dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
     dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j-1][0] + dp[i-1][j-1][1]

    '''
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        dp[0][0][0] = 1
        for i in range(1, n):
            for j in range(k + 1):
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % mod
                dp[i][j][1] = dp[i-1][j][1]
                if j > 0:
                    dp[i][j][1] += dp[i-1][j-1][0]
                    dp[i][j][1] %= mod
                    dp[i][j][1] += dp[i-1][j-1][1]
                    dp[i][j][1] %= mod
        return (dp[n-1][k][0] + dp[n-1][k][1]) % mod

print(Solution().numberOfSets(4, 2))