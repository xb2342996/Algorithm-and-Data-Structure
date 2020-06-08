## written by xiongbiao
## date 2020-6-8

'''
给定一个字符串s，找到其中最长的回文子序列，并返回该序列的长度。可以假设s的最大长度为1000。
'''
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()
        n = len(pairs)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)