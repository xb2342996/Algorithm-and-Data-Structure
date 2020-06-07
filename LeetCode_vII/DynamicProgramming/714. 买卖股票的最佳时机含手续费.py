## written by xiongbiao
## date 2020-6-6

'''
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
'''
class Solution(object):
    '''
    k次交易 第i天 0表示卖出不持有 1表示买入持有
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + price[i])
    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - price[i])
    base case:
    dp[i][0][0] = dp[-1][k][0] = 0
    dp[i][0][1] = dp[-1][k][1] = -inf
    '''
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices) + 1
        dp = [[0, 0]] * n
        dp[0] = [0, float('-inf')]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i-1] - fee)

        return dp[n][0]
