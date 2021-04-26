"""
@author: xiongbiao
@date: 2021-04-19 21:17
"""

class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # ans = -1
        # length = len(nums)
        # for i in range(length):
        #     for j in range(i + 1, length):
        #         temp = nums[i] + nums[j]
        #         if temp < k and temp > ans:
        #             ans = temp
        #
        # return ans

        nums.sort()
        left, right = 0, len(nums) - 1
        ans = -1
        while left < right:
            if nums[left] + nums[right] < k:
                ans = max(nums[left] + nums[right], ans)
                left += 1
            else:
                right -= 1

        return ans



print(Solution().twoSumLessThanK(nums = [34,23,1,24,75,33,54,8], k = 15))