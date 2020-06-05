## written by xiongbiao
## date 2020-6-5

'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''
class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    '''
    动态规划
    dp[i] = d[i-1] + dp[i-2] 初始状态：dp[1] = 1 dp[2] = 2
    '''
    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     dp = [0] * (n + 1)
    #     dp[1] = 1
    #     dp[2] = 2
    #
    #     for i in range(3, n + 1):
    #         dp[i] = dp[i - 1] + dp[i - 2]
    #
    #     return dp[-1]

Solution().climbStairs(3)
