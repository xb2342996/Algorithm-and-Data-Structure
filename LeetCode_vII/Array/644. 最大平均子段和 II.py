## written by xiongbiao
## date 2020-5-28
'''
给定一个包含 n 个整数的数组，找到最大平均值的连续子序列，且长度大于等于 k。并输出这个最大平均值。
'''

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxVal = float('-inf')
        minVal = float('inf')
        for n in nums:
            maxVal = max(maxVal, n)
            minVal = min(minVal, n)

        prevVal = maxVal
        error = float('inf')
        while error > 0.00001:
            mid = (maxVal + minVal) * 0.5
            print(mid)
            if self.check(nums, mid, k):
                minVal = mid
            else:
                maxVal = mid
            error = abs(prevVal - mid)
            prevVal = mid

        return minVal


    def check(self, nums, val, k):
        sum = 0
        prev = 0
        min_sum = 0
        for i in range(k):
            sum += nums[i] - val
        if sum > 0:
            return True
        for i in range(k, len(nums)):
            sum += nums[i] - val
            prev += nums[i - k] - val
            min_sum = min(prev, min_sum)
            if sum > min_sum:
                return True

        return False

nums = [1,12,-5,-6,50,3]
k = 4
print(Solution().findMaxAverage(nums, k))