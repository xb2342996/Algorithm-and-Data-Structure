"""
@author: xiongbiao
@date: 2021-04-26 22:07
"""
'''
给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。
'''
'''
解题思路：
数字求和问题思路：暴力法复杂度取决于多少个数字的和，降低复杂度的手段，排序（不等式问题）后使用双指针获取区间范围，排序的目的是使得数组变成有序的，只要右指针指向的元素符合条件，前面所有的元素都符合，通过索引即可算出范围
'''

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def twoSum(nums, index, rest):
            l, r = index, len(nums) - 1
            total = 0
            while l < r:
                if nums[l] + nums[r] < rest:
                    total += r - l
                    l += 1
                else:
                    r -= 1
            return total

        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(0, n - 2):
            ans += twoSum(nums, i + 1, target - nums[i])
        return ans


print(Solution().threeSumSmaller([-1, 1, -1, -1], -1))