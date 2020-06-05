## written by xiongbiao
## date 2020-6-5

'''
有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，每个栅栏柱可以用其中一种颜色进行上色。
'''
class Solution(object):
    '''
    dp[i] = (dp[i-1] +dp[i-2]) * (k-1)
    dp[0] = k  dp[1] = k * k
    第一个栅栏有k种涂法， 第二个有k*k种涂法，第三个只能有k-1种选择（要么第一个和第二个同颜色，要么第一个和第二个不同颜色）
    '''
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k

        dp = [0] * n
        dp[0] = k
        dp[1] = k * k

        for i in range(2, n):
            dp[i] = (dp[i-1] + dp[i-2]) * (k - 1)

        return dp[-1]