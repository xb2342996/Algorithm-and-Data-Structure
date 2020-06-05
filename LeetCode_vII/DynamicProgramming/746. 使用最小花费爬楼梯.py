## written by xiongbiao
## date 2020-6-5

'''
数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
'''
class Solution(object):
    '''
    dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    返回dp[-1]或dp[-2]中小的那个
    '''
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * len(cost)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[-1], dp[-2])

Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])