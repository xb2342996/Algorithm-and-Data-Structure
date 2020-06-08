## written by xiongbiao
## date 2020-6-8

'''
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices) + 1
        dp = [[0, 0]] * n
        dp[0] = [0, float('-inf')]
        freeze = 0
        for i in range(1, n):
            temp = dp[i - 1][0]
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
            dp[i][1] = max(dp[i-1][1], freeze - prices[i-1])
            freeze = temp
        return dp[-1][0]
print(Solution().maxProfit([1,2,3,0,2]))