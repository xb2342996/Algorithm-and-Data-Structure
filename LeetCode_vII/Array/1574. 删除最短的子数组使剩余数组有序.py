"""
@author: xiongbiao
@date: 2021-04-24 21:40
"""

'''
给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。
一个子数组指的是原数组中连续的一个子序列。
请你返回满足题目要求的最短子数组的长度。
'''
'''
思路：
整体单调递增，提取局部单调区间，并合并单调区间，获得整体单调性。
'''

class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)
        left = 0
        while left < length - 1 and arr[left] <= arr[left + 1]:
            left += 1

        if left == length - 1:
            return 0

        right = length - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        ans = min(length - left - 1, right)
        i, j = 0, right
        while i < left + 1 and j < length:
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1
        return ans



print(Solution().findLengthOfShortestSubarray([5,4,3,2,1]))