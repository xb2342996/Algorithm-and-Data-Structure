# written by xiongbiao
# date 2020-11-22
'''
给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
'''

class Solution(object):
    '''
    dp[i][j] 表示num[i] mod k 等于 j的最大和
    '''
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0] * 3 for _ in range(len(nums) + 1)]
        dp[0][1] = float('-inf')
        dp[0][2] = float('-inf')

        for i in range(1, len(nums) + 1):
            if nums[i-1] % 3 == 0:
                dp[i][0] = max(dp[i-1][0], dp[i-1][0] + nums[i-1])
                dp[i][1] = max(dp[i-1][1], dp[i-1][1] + nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][2] + nums[i-1])
            elif nums[i-1] % 3 == 1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][2] + nums[i-1])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] + nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][1] + nums[i-1])
            elif nums[i-1] % 3 == 2:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + nums[i-1])
                dp[i][1] = max(dp[i-1][1], dp[i-1][2] + nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][0] + nums[i-1])

        return dp[len(nums)][0]
print(Solution().maxSumDivThree([3,6,5,1,8]))