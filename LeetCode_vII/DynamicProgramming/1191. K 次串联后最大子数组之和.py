"""
@author: xiongbiao
@date: 2021-01-23 20:04
"""
'''
给你一个整数数组 arr 和一个整数 k。
首先，我们要对该数组进行修改，即把原数组 arr 重复 k 次。
举个例子，如果 arr = [1, 2] 且 k = 3，那么修改后的数组就是 [1, 2, 1, 2, 1, 2]。
然后，请你返回修改后的数组中的最大的子数组之和。
注意，子数组长度可以是 0，在这种情况下它的总和也是 0。
由于 结果可能会很大，所以需要 模（mod） 10^9 + 7 后再返回。 
'''

class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        mod = 10 ** 9 + 7
        max_pre = float('-inf')
        max_suf = float('-inf')
        max_sub = float('-inf')
        sum = 0
        for i in range(0, len(arr)):
            sum += arr[i]
            max_pre = max(sum, max_pre)

        sum = 0
        for i in range(len(arr) - 1, -1, -1):
            sum += arr[i]
            max_suf = max(sum, max_suf)

        prev = 0
        for i in range(0, len(arr)):
            if prev > 0:
                prev += arr[i]
            else:
                prev = arr[i]
            max_sub = max(max_sub, prev)

        ans = max(max_sub, max_pre, max_suf)
        if k > 1:
            ans = max(ans, max_pre + max_suf)
            ans = max(ans, max_suf + max_pre + sum * (k-2))

        return ans % mod if ans > 0 else 0

print(Solution().kConcatenationMaxSum([-5,4,-4,-3,5,-3], 3))