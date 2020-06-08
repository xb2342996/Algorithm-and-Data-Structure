## written by xiongbiao
## date 2020-6-7

'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
'''
class Solution(object):
    '''

    '''
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        dp = 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp += 1
                ans += dp
            else:
                dp = 0
        # print(ans)
        return ans
    '''
    动态规划，时间O（n）空间O（n）
    '''
    # def numberOfArithmeticSlices(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: int
    #     """
    #     ans = 0
    #     dp = [0] * len(A)
    #     for i in range(2, len(A)):
    #         if A[i] - A[i-1] == A[i-1] - A[i-2]:
    #             dp[i] = 1 + dp[i-1]
    #             ans += dp[i]
    #     print(ans)
    #     return ans
    '''
    暴力解法，时间O（n^2) 空间O（1）
    '''
    # def numberOfArithmeticSlices(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: int
    #     """
    #     l = len(A)
    #     ans = 0
    #     for i in range(1, l):
    #         diff = A[i] - A[i-1]
    #         for j in range(i, l-1):
    #             if A[j + 1] - A[j] == diff:
    #                 ans += 1
    #             else:
    #                 break
    #
    #
    #     print(ans)

Solution().numberOfArithmeticSlices([1,3,5,7,9])