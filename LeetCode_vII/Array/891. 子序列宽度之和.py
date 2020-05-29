## written by xiongbiao
## date 2020-5-27

'''
给定一个整数数组 A ，考虑 A 的所有非空子序列。
对于任意序列 S ，设 S 的宽度是 S 的最大元素和最小元素的差。
返回 A 的所有子序列的宽度之和。
'''

class Solution(object):
    '''
    数学公式：sum((2^i - 2^(length-i-1)) * i)
    '''
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        mod = 10 ** 9 + 7
        length = len(A)
        A.sort()

        pow = [1]
        for i in range(1, length):
            pow.append((pow[-1] << 1) % mod)

        ans = 0
        for i, x in enumerate(A):
            ans = (ans + (pow[i] - pow[length - i - 1]) * x) % mod
        return ans


