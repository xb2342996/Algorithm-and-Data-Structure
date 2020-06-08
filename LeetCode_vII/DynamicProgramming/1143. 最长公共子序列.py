## written by xiongbiao
## date 2020-6-7
'''
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
'''

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        m, n = len(text1) + 1, len(text2) + 1

        dp = [0] * n
        topLeft = dp[0]
        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:
                    dp[j] = topLeft + 1
                else:
                    topLeft = dp[j]
                    dp[j] = max(dp[j], dp[j - 1])

        return dp[-1]

    # def longestCommonSubsequence(self, text1, text2):
    #     """
    #     :type text1: str
    #     :type text2: str
    #     :rtype: int
    #     """
    #     m, n = len(text1) + 1, len(text2) + 1
    #     dp = [[0] * n for _ in range(m)]
    #
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             if text1[i-1] == text2[j-1]:
    #                 dp[i][j] = dp[i-1][j-1] + 1
    #             else:
    #                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #
    #     # print(dp[-1][-1])
    #
    #     return dp[-1][-1]

Solution().longestCommonSubsequence('abc', 'abc')