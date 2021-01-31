"""
@author: xiongbiao
@date: 2021-01-11 21:36
"""

'''
给定一个字符串 S，计算 S 的不同非空子序列的个数。
因为结果可能很大，所以返回答案模 10^9 + 7.
'''
class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [1]
        last = {}
        for i, s in enumerate(S):
            dp.append(dp[-1] * 2)
            if s in last:
                dp[-1] -= dp[last[s]]
            last[s] = i

        return (dp[-1] - 1) % (10 ** 9 + 7)

print(Solution().distinctSubseqII('aaa'))