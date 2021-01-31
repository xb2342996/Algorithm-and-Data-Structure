"""
@author: xiongbiao
@date: 2021-01-24 15:08
"""

'''
给你一个整数数组 arr 和一个整数 difference，请你找出并返回 arr 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 difference 。
'''

class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        # dp = [1] * len(arr)
        # timeout
        # for i in range(1, len(arr)):
        #     for j in range(i):
        #         if arr[i] - arr[j] == difference:
        #             dp[i] = dp[j] + 1
        dp = {}
        ans = 0
        for i in range(len(arr)):
            if (arr[i] - difference) in dp:
                dp[arr[i]] = dp[arr[i] - difference] + 1
            else:
                dp[arr[i]] = 1
            ans = max(ans, dp[arr[i]])
        print(dp)
        print(ans)

print(Solution().longestSubsequence([1,5,7,8,5,3,4,2,1], -2))