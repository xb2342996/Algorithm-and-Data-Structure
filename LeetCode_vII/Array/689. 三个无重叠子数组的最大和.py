## written by xiongbiao
## date 2020-5-29
'''
给定数组 nums 由正整数组成，找到三个互不重叠的子数组的最大和。
每个子数组的长度为k，我们要使这3*k个项的和最大化。
返回每个区间起始索引的列表（索引从 0 开始）。如果有多个结果，返回字典序最小的一个。
'''

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = len(nums)
        sums = [0] * (l - k + 1)
        sum = 0
        for i in range(l):
            sum += nums[i]
            if i >= k:
                sum -= nums[i - k]
            if i >= k - 1:
                sums[i - k + 1] = sum
        # print([i for i in range(len(sums))])
        # print(sums)
        best = 0
        left = [0] * len(sums)
        for i in range(len(sums)):
            if sums[best] < sums[i]:
                best = i
            left[i] = best

        best = len(sums) - 1
        right = [0] * len(sums)
        for i in range(len(sums))[::-1]:
            if sums[best] <= sums[i]:
                best = i
            right[i] = best

        # print(left)
        # print(right)
        ans = [-1, -1, -1]
        for i in range(k, len(sums) - k):
            l = left[i - k]
            r = right[i + k]
            # print(l, i, r)
            if ans[0] == -1 or sums[l] + sums[i] + sums[r] > sums[ans[0]] + sums[ans[1]] + sums[ans[2]]:
                ans = [l, i, r]

        return ans

Solution().maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)
