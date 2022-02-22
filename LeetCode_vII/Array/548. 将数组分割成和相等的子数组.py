"""
@author: xiongbiao
@date: 2021-05-04 21:30
"""
'''
给定一个有 n 个整数的数组，你需要找到满足以下条件的三元组 (i, j, k) ：
0 < i, i + 1 < j, j + 1 < k < n - 1
子数组 (0, i - 1)，(i + 1, j - 1)，(j + 1, k - 1)，(k + 1, n - 1) 的和应该相等。
这里我们定义子数组 (L, R) 表示原数组从索引为L的元素开始至索引为R的元素。
'''
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # n = len(nums)
        # for i in range(1, n - 5):
        #     for j in range(i + 2, n - 3):
        #         for k in range(j + 2, n - 1):
        #             # print(i, j, k)
        #             if sum(nums[0:i]) == sum(nums[i+1:j]) == sum(nums[j+1:k]) == sum(nums[k+1:n]):
        #                 return True
        # return False
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        for m in range(3, n - 3):
            helper = set()
            for l in range(1, m):
                a = prefix_sum[l-1]
                b = prefix_sum[m-1] - prefix_sum[l]
                if a == b:
                    helper.add(a)
            for r in range(m + 2, n - 1):
                c = prefix_sum[r-1] - prefix_sum[m]
                d = prefix_sum[n-1] - prefix_sum[r]
                if c == d and c in helper:
                    return True
        return False

print(Solution().splitArray([1,2,1,3,0,0,2,2,1,3,3]))
