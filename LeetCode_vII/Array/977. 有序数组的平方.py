"""
@author: xiongbiao
@date: 2021-04-20 21:30
"""

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        ans = [0] * length

        left, right = 0, length - 1
        pos = length - 1
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                ans[pos] = nums[right] ** 2
                right -= 1
            else:
                ans[pos] = nums[left] ** 2
                left += 1
            pos -= 1
        return ans

print(Solution().sortedSquares([-4,-1,0,3,10]))
