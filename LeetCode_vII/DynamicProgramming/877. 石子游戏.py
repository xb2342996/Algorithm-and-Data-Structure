## written by xiongbiao
## date 2020-6-5
'''
亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
'''

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[(0, 0)] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = (piles[i], 0)

        for i in range(2, n + 1):
            for j in range(0 , n - i + 1):
                m = i + j - 1
                left = piles[j] + dp[j + 1][m][1]
                right = piles[m] + dp[j][m - 1][1]
                if left > right:
                    dp[j][m] = (left, piles[j] + dp[j+1][m][0])
                else:
                    dp[j][m] = (piles[m] + dp[j][m-1][0], right)

        return dp[0][n-1][0] > 0


print(Solution().stoneGame([5,4,3,5]))
