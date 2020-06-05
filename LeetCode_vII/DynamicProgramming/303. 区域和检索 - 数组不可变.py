## written by xiongbiao
## date 2020-6-5

'''
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
'''

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.preSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.preSum[i+1] = self.preSum[i] + nums[i]
        print(self.preSum)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.preSum[j+1] - self.preSum[i]


n = NumArray([-2, 0, 3, -5, 2, -1])
print(n.sumRange(0, 2))
print(n.sumRange(2, 5))
print(n.sumRange(0, 5))
