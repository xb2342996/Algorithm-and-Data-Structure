"""
@author: xiongbiao
@date: 2021-01-31 21:40
"""
'''
给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：
给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
总成本必须恰好等于 target 。
添加的数位中没有数字 0 。
由于答案可能会很大，请你以字符串形式返回。
如果按照上述要求无法得到任何整数，请你返回 "0" 。
'''
class Solution(object):
    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        dp = [0] + [float('-inf')] * target

        for i in range(9, 0, -1):
            for j in range(1, target + 1):
                if j >= cost[i-1]:
                    dp[j] = max(dp[j], dp[j - cost[i - 1]] * 10 + i)
        return str(dp[-1]) if dp[-1] > 0 else '0'

Solution().largestNumber([4,3,2,5,6,7,2,5,5], target = 9)