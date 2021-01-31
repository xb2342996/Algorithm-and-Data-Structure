"""
@author: xiongbiao
@date: 2021-01-23 18:58
"""
'''
给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。
换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。
注意，删除一个元素后，子数组 不能为空。
'''
class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        prefix = [float('inf')] * len(arr)
        suffix = [float('inf')] * len(arr)
        prefix[0] = arr[0]
        suffix[-1] = arr[-1]
        for i in range(1, len(arr)):
            prefix[i] = max(prefix[i - 1] + arr[i], arr[i])

        for i in range(len(arr) - 2, -1, -1):
            suffix[i] = max(suffix[i + 1] + arr[i], arr[i])

        ans = max(prefix)

        for i in range(1, len(arr) - 1):
            ans = max(ans, suffix[i + 1] + prefix[i - 1])

        return ans


Solution().maximumSum([1, -2, 0, 3])