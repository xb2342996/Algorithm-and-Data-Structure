"""
@author: xiongbiao
@date: 2021-05-17 21:45
"""
'''
给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。
在此处，环形数组意味着数组的末端将会与开头相连呈环状。（形式上，当0 <= i < A.length 时 C[i] = A[i]，且当 i >= 0 时 C[i+A.length] = C[i]）
此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。（形式上，对于子数组 C[i], C[i+1], ..., C[j]，不存在 i <= k1, k2 <= j 其中 k1 % A.length = k2 % A.length）
'''

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_val = float('-inf')
        for i in range(n):
            val = max(max_val, 0) + nums[i]
            max_val = max(max_val, val)

        if max_val < 0:
            return max_val

        min_val = float('inf')
        for i in range(n):
            val = min(0, min_val) + nums[i]
            min_val = min(val, min_val)

        return max(max_val, sum(nums) - min_val)


Solution().maxSubarraySumCircular([1,-2,3,-2])