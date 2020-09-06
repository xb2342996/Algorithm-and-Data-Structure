## written by xiongbiao
## date 2020-9-6
'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            maxLen = 1
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    maxLen = max(maxLen, dp[j] + 1)
            dp[i] = maxLen

        return max(dp)


print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))
