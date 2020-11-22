# written by xiongbiao
# date 2020-11-22

'''
给定一个整数数组 A，返回 A 中最长等差子序列的长度。
回想一下，A 的子序列是列表 A[i_1], A[i_2], ..., A[i_k] 其中 0 <= i_1 < i_2 < ... < i_k <= A.length - 1。并且如果 B[i+1] - B[i]( 0 <= i < B.length - 1) 的值都相同，那么序列 B 是等差的。
'''

class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        diffs = [{}]
        ans = 1
        for i in range(1, length):
            sub_diff = {}
            for j in range(0, i):
                diff = A[i] - A[j]
                if diff in diffs[j]:
                    sub_diff[diff] = diffs[j][diff] + 1
                    ans = max(ans, sub_diff[diff])
                else:
                    sub_diff[diff] = 1
            diffs.append(sub_diff)
        return ans + 1
print(Solution().longestArithSeqLength([20,1,15,3,10,5,8]))