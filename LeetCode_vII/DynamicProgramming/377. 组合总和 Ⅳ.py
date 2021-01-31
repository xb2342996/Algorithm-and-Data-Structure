'''
@author: xiongbiao
@date: 2021-01-10 10:13
'''

'''
给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。
'''
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for n in nums:
                if i >= n:
                    dp[i] += dp[i-n]

        return dp[-1]

print(Solution().combinationSum4(nums = [1, 2, 3], target = 4))