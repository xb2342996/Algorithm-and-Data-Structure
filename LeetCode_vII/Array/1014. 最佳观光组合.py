"""
@author: xiongbiao
@date: 2021-05-24 22:21
"""
'''
给你一个正整数数组 values，其中 values[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的 距离 为 j - i。
一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离。
返回一对观光景点能取得的最高分。
'''

class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        n = len(values)
        max_val = 0
        max_score = 0
        for i in range(n):
            max_score = max(max_score, max_val + values[i] - i)
            max_val = max(max_val, values[i] + i)

        return max_score


s = Solution().maxScoreSightseeingPair([8,1,5,2,6])
print(s)

s = Solution().maxScoreSightseeingPair([1, 2])
print(s)

s = Solution().maxScoreSightseeingPair([100, 29, 45, 33, 97, 98])
print(s)

s = Solution().maxScoreSightseeingPair([1, 3, 5])
print(s)