## written by xiongbiao
## date 2020-6-8

'''
给定一个字符串s，找到其中最长的回文子序列，并返回该序列的长度。可以假设s的最大长度为1000。
'''
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        dp = [[0] * l for _ in range(l)]
        for i in range(l):
            dp[i][i] = 1

        for i in range(l)[::-1]:
            for j in range(i+1, l):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][l-1]

print(Solution().longestPalindromeSubseq('bbbbb'))