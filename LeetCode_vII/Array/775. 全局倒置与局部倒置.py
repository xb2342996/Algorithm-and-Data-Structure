"""
@author: xiongbiao
@date: 2021-05-08 21:46
"""
'''
给你一个长度为 n 的整数数组 nums ，表示由范围 [0, n - 1] 内所有整数组成的一个排列。
全局倒置 的数目等于满足下述条件不同下标对 (i, j) 的数目：
0 <= i < j < n
nums[i] > nums[j]
局部倒置 的数目等于满足下述条件的下标 i 的数目：
0 <= i < n - 1
nums[i] > nums[i + 1]
当数组 nums 中 全局倒置 的数量等于 局部倒置 的数量时，返回 true ；否则，返回 false 。
'''
class Solution(object):
    def isIdealPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # n = len(nums)
        # g, l = 0, 0
        # for i in range(n - 1):
        #     for j in range(i+1, n):
        #         if nums[i] > nums[j]:
        #             g += 1
        #
        # for i in range(n - 1):
        #     if nums[i] > nums[i + 1]:
        #         l += 1
        #
        # if l == g:
        #     return True
        # else:
        #     return False
        for i, x in enumerate(nums):
            if abs(i - x) > 1:
                return False
        return True

print(Solution().isIdealPermutation([1,2,0]))