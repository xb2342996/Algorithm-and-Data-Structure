## written by xiongbiao
## date 2020-6-8

'''
在一个小城市里，有 m 个房子排成一排，你需要给每个房子涂上 n 种颜色之一（颜色编号为 1 到 n ）。有的房子去年夏天已经涂过颜色了，所以这些房子不需要被重新涂色。
我们将连续相同颜色尽可能多的房子称为一个街区。（比方说 houses = [1,2,2,3,3,2,1,1] ，它包含 5 个街区  [{1}, {2,2}, {3,3}, {2}, {1,1}] 。）
给你一个数组 houses ，一个 m * n 的矩阵 cost 和一个整数 target ，其中：
houses[i]：是第 i 个房子的颜色，0 表示这个房子还没有被涂色。
cost[i][j]：是将第 i 个房子涂成颜色 j+1 的花费。
请你返回房子涂色方案的最小总花费，使得每个房子都被涂色后，恰好组成 target 个街区。如果没有可用的涂色方案，请返回 -1 。
'''
class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        dp = [[[float('inf')] * (target+1) for _ in range(n+1)] for _ in range(m)]

        if houses[0] == 0:
            for i in range(1, n+1):
                dp[0][i][0] = cost[0][i-1]
        else:
            dp[0][houses[0]][0] = 0

        for i in range(1, m):
            for j in range(1, n+1):
                for t in range(target):
                    if houses[i] == 0:
                        for k in range(1, n+1):
                            if dp[i - 1][k][t] == float('inf'):
                                continue
                            if k == j:
                                dp[i][j][t] = min(dp[i-1][k][t] + cost[i][j-1], dp[i][j][t])
                            else:
                                dp[i][j][t+1] = min(dp[i-1][k][t] + cost[i][j-1], dp[i][j][t+1])
                    else:
                        if dp[i-1][j][t] == float('inf'):
                            continue
                        if houses[i] == j:
                            dp[i][j][t] = min(dp[i-1][j][t], dp[i][j][t])
                        else:
                            dp[i][houses[i]][t+1] = min(dp[i-1][j][t], dp[i][houses[i]][t+1])

        ans = float('inf')
        for i in range(1, n + 1):
            ans = min(ans, dp[-1][i][target-1])

        return -1 if ans == float('inf') else ans

print(Solution().minCost([0,0,0,0,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5,2,3))