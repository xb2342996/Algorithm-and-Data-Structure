"""
@author: xiongbiao
@date: 2021-05-07 21:29
"""
'''
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
'''

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # row, col = len(A), len(B)
        #
        # matrix = [[0] * (col + 1) for _ in range(row + 1)]
        # ans = 0
        # for i in range(1, row + 1):
        #     for j in range(1, col + 1):
        #         if A[i - 1] == B[j - 1]:
        #             matrix[i][j] = matrix[i-1][j-1] + 1
        #             ans = max(ans, matrix[i][j])
        #
        # return ans


print(Solution().findLength([1,2,3,2,1], [3,2,1,4,7]))