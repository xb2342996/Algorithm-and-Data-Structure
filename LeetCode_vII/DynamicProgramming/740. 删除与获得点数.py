"""
@author: xiongbiao
@date: 2021-01-10 14:45
"""
'''
给定一个整数数组 nums ，你可以对它进行一些操作。
每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。
开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
'''

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        length = max(nums)
        counters = [0] * (length + 1)

        for n in nums:
            counters[n] += 1

        dp = [0] * (length + 1)
        for i, c in enumerate(counters):
            if i < 2:
                dp[i] = i * c
            else:
                dp[i] = max(dp[i-1], dp[i - 2] + i * c)

        return dp[-1]

print(Solution().deleteAndEarn([]))