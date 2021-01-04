# written by xiong biao
# date 2021-01-04

'''
给定一个包含 非负数 的数组和一个目标 整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，且总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。
'''

class Solution(object):
    '''
    技巧：2个前缀和 mod k有相同的余数，2个前缀和的区间就是能被k整除的最小连续子数组
    '''
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        rest = {0 : -1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            if k != 0:
                total %= k
            if total not in rest:
                rest[total] = i
            else:
                if i - rest[total] > 0:
                    return True

        return False

print(Solution().checkSubarraySum([23,2,4,6,7], k = 0))