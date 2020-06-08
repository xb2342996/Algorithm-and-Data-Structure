## written by xiongbiao
## date 2020-6-7
'''
给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。
下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。
'''
class Solution(object):
    '''
    动态规划 时间复杂度O（n^2) 空间复杂度O（n）
    '''
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])
        dp = [0] * cols
        for i in range(cols):
            dp[i] = A[0][i]
        prev = dp[0]
        for i in range(1, rows):
            for j in range(cols):
                prev, dp[j] = dp[j], min(prev, dp[j], dp[min(cols-1, j + 1)]) + A[i][j]
            prev = dp[0]
        return min(dp)
    '''
    时间O（n^2) 空间O（n^2)
    '''
    # def minFallingPathSum(self, A):
    #     """
    #     :type A: List[List[int]]
    #     :rtype: int
    #     """
    #     rows, cols = len(A), len(A[0])
    #     dp = [[0] * cols for _ in range(rows)]
    #     for i in range(cols):
    #         dp[0][i] = A[0][i]
    #
    #     for i in range(1, rows):
    #         for j in range(cols):
    #
    #             dp[i][j] = min(dp[i - 1][max(0, j - 1)], dp[i - 1][j], dp[i - 1][min(cols-1, j + 1)]) + A[i][j]
    #
    #     return min(dp[-1])
Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])


