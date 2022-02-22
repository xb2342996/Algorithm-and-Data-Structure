"""
@author: xiongbiao
@date: 2021-05-18 21:45
"""
'''
如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，那么该字符串是单调递增的。
我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。
返回使 S 单调递增的最小翻转次数。
'''

class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        one, zero = 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                zero, one = zero + 1, min(zero, one)
            else:
                one = min(zero, one) + 1

        return min(one, zero)

print(Solution().minFlipsMonoIncr('010110'))