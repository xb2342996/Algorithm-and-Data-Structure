## written by xiongbiao
## date 2020-6-5

'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
'''
class Solution(object):
    '''
    单调栈 + sentinel
    '''
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        prices.append(-1)
        for price in prices:
            while stack and stack[-1] < price:
                ans = max(ans, stack[-1] - stack[0])
                stack.pop()
            stack.append(price)

        return ans
    '''
    动态规划，获取最小值，用当前值-最小值
    '''
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     min_price = float('inf')
    #     max_profile = 0
    #
    #     for i in range(0, len(prices)):
    #         max_profile = max(max_profile, prices[i] - min_price)
    #         min_price = min(prices[i], min_price)
    #
    #     return max_profile


print(Solution().maxProfit([7,1,5,3,6,4]))