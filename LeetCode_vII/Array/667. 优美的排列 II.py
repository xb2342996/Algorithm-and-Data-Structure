"""
@author: xiongbiao
@date: 2021-05-05 21:09
"""
'''
给定两个整数 n 和 k，你需要实现一个数组，这个数组包含从 1 到 n 的 n 个不同整数，同时满足以下条件：
① 如果这个数组是 [a1, a2, a3, ... , an] ，那么数组 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 中应该有且仅有 k 个不同整数；.
② 如果存在多种答案，你只需实现并返回其中任意一种.
'''

class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        # ans = [i for i in range(1, n+1)]
        # for i in range(1, k):
        #     ans = ans[:i] + ans[i:][::-1]
        # return ans

        

print(Solution().constructArray(3, 1))