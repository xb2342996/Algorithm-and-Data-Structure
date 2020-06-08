## written by xiongbiao
## date 2020-6-7
'''
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
'''
class Solution(object):
    '''
    动态规划 时间复杂度O（n^2) 空间复杂度O(N)
    '''
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i-j), j * dp[i-j])

        print(dp)
        return dp[-1]
    '''     
    记忆化递归，避免不必要的重复计算
    '''
    # def integerBreak(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     self.memory = [0] * (n + 1)
    #     return self.breakNum(n)
    #
    # def breakNum(self, n):
    #     if n == 2:
    #         return 1
    #     if self.memory[n] != 0:
    #         return self.memory[n]
    #     res = -1
    #     for i in range(1, n-1):
    #         res = max(res, self.breakNum(n - i), i * (n - i))
    #     self.memory[n] = res
    #     return res
    '''
    递归遍历
    '''
    # def integerBreak(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 2:
    #         return 1
    #
    #     res = -1
    #     for i in range(1, n-1):
    #         res = max(res, i * self.integerBreak(n - i), i * (n - i))
    #     return res

Solution().integerBreak(10)