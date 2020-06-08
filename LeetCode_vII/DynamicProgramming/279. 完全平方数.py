## written by xiongbiao
## date 2020-6-7
'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
'''
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        maxSquare = math.floor(math.sqrt(n))
        squares = [i ** 2 for i in range(1, maxSquare + 1)]
        dp = [float('inf')] * (n + 1)
        for i in range(len(squares)):
            dp[squares[i]] = 1

        for i in range(2, n + 1):
            for j in range(len(squares)):
                if i < squares[j]:
                    break
                dp[i] = min(dp[i-squares[j]] + 1, dp[i])
        return dp[-1]
print(Solution().numSquares(13))