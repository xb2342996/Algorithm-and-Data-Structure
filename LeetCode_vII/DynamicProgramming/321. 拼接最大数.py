"""
@author: xiongbiao
@date: 2021-02-14
"""
'''
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
说明: 请尽可能地优化你算法的时间和空间复杂度。
'''
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = 0
        output = []
        for i in range(k + 1):
            res = 0
            j = k - i
            if i > len(nums1) or j > len(nums2):
                continue

            l1 = self.maxSubseq(i, nums1)
            l2 = self.maxSubseq(j, nums2)
            print(l1, l2)
            merged = self.merge(l1, l2)
            for n in merged:
                res = res * 10 + n
            if res > ans:
                ans = res
                output = merged
        return output


    def maxSubseq(self, k, nums):
        stack = [0] * k
        remains = len(nums) - k
        top = -1
        for i, n in enumerate(nums):
            while top >= 0 and stack[top] < n and remains > 0:
                top -= 1
                remains -= 1
            if top < k - 1:
                top += 1
                stack[top] = n
            else:
                remains -= 1
        return stack

    def merge(self, l1, l2):
        if len(l1) == 0:
            return l2
        if len(l2) == 0:
            return l1

        merged_length = len(l1) + len(l2)
        p1 = 0
        p2 = 0
        l = []
        for i in range(merged_length):
            if self.compare(l1, p1, l2, p2) > 0:
                l.append(l1[p1])
                p1 += 1
            else:
                l.append(l2[p2])
                p2 += 1
            print(l, p1, p2)
        return l

    def compare(self, s1, i1, s2, i2):
        while i1 < len(s1) and i2 < len(s2):
            diff = s1[i1] - s2[i2]
            if diff != 0:
                return diff
            i1 += 1
            i2 += 1
        return len(s1) - i1 - len(s2) + i2

print(Solution().maxNumber(nums1 = [6,5],nums2 = [6,0,4],k = 5))
