"""
@author: xiongbiao
@date: 2021-05-16 21:27
"""
'''
给定一个数组 A，将其划分为两个连续子数组 left 和 right， 使得：
left 中的每个元素都小于或等于 right 中的每个元素。
left 和 right 都是非空的。
left 的长度要尽可能小。
在完成这样的分组后返回 left 的长度。可以保证存在这样的划分方法。
'''

class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix = [nums[0]] * n
        suffix = [nums[-1]] * n
        for x in range(1, n):
            if nums[x] > prefix[x-1]:
                prefix[x] = nums[x]
            else:
                prefix[x] = prefix[x-1]

        for x in range(n - 2, -1, -1):
            if nums[x] < suffix[x + 1]:
                suffix[x] = nums[x]
            else:
                suffix[x] = suffix[x + 1]

        for i in range(n - 1):
            if prefix[i] <= suffix[i + 1]:
                return i + 1

print(Solution().partitionDisjoint([5,0,3,8,6]))