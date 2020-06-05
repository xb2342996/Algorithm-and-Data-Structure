## written by xiongbiao
## date 2020-6-5

'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
'''
class Solution(object):
    '''
    分治
    '''
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        left_max = self.maxSubArray(nums[0:mid])
        right_max = self.maxSubArray(nums[mid:])

        max_left_part = float('-inf')
        tmp = 0
        for i in range(mid)[::-1]:
            tmp += nums[i]
            max_left_part = max(max_left_part, tmp)

        tmp = 0
        max_right_part = float('-inf')
        for i in range(mid, len(nums)):
            tmp += nums[i]
            max_right_part = max(max_right_part, tmp)

        total = max_right_part + max_left_part
        return max(total, left_max, right_max)


    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     dp = [0] * len(nums)
    #     max_val = dp[0] = nums[0]
    #     for i in range(1, len(nums)):
    #         # prev = dp[i - 1]
    #         # if prev > 0:
    #         #     dp[i] = prev + nums[i]
    #         # else:
    #         #     dp[i] = nums
    #         dp[i] = max(dp[i - 1] + nums[i], nums[i])
    #         max_val = max(max_val, dp[i])
    #
    #     return max_val
    '''
    暴力解法
    '''
    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     max_val = float('-inf')
    #     for i in range(len(nums)):
    #         for j in range(i, len(nums)):
    #             max_val = max(max_val, sum(nums[i:j]))
    #
    #     return max_val

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))