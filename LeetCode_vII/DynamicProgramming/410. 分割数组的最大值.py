"""
@author: xiongbiao
@date: 2021-03-07 14:41
"""

'''
给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。
设计一个算法使得这 m 个子数组各自和的最大值最小。
'''

class Solution(object):
    # def splitArray(self, nums, m):
    #     """
    #     :type nums: List[int]
    #     :type m: int
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    #     prefix = [0] * (n + 1)
    #     for i in range(1, n + 1):
    #         prefix[i] = prefix[i-1] + nums[i-1]
    #
    #     dp[0][0] = 0
    #     for i in range(1, n + 1):
    #         for j in range(1, min(m, i) + 1):
    #             for k in range(i):
    #                 dp[i][j] = min(dp[i][j], max(dp[k][j-1], prefix[i] - prefix[k]))
    #     return dp[n][m]

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        def check(n):
            total = 0
            count = 1
            for num in nums:
                if total + num > n:
                    count += 1
                    total = num
                else:
                    total += num

            return count <= m

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

print(Solution().splitArray([1,2,3,4,5], 3))