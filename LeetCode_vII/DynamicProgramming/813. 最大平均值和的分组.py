"""
@author: xiongbiao
@date: 2021-01-10 19:37
"""

'''
我们将给定的数组 A 分成 K 个相邻的非空子数组 ，我们的分数由每个子数组内的平均值的总和构成。计算我们所能得到的最大分数是多少。
注意我们必须使用 A 数组中的每一个数进行分组，并且分数不一定需要是整数。
'''
class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        S = [0]
        for a in A:
            S.append(S[-1] + a)
        def avg(i, j):
            return (S[j] - S[i]) / float(j - i)

        N = len(A)
        dp = [avg(i, N) for i in range(N)]
        for i in range(K - 1):
            for j in range(N):
                for k in range(j + 1, N):
                    dp[j] = max(dp[j] + avg(j, k) + dp[k])

        return dp[0]

