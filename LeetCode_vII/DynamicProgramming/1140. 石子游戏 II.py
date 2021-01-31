"""
@author: xiongbiao
@date: 2021-01-23 14:43
"""
'''
亚历克斯和李继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。
亚历克斯和李轮流进行，亚历克斯先开始。最初，M = 1。
在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。
游戏一直持续到所有石子都被拿走。
假设亚历克斯和李都发挥出最佳水平，返回亚历克斯可以得到的最大数量的石头。
'''

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        length = len(piles)
        dp = [[0] * (length + 1) for _ in range(length)]
        prefix = 0

        for i in range(length - 1, -1, -1):
            prefix += piles[i]
            for j in range(1, length + 1):
                print('i:', i, 'j:',j ,'index:', i + 2 * j)
                if i + 2 * j >= length:
                    dp[i][j] = prefix
                else:
                    for k in range(1, 2 * j + 1):
                        dp[i][j] = max(dp[i][j], prefix - dp[i + k][max(j, k)])
        return dp[0][1]

print(Solution().stoneGameII([2, 7, 9, 4, 4]))