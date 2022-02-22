"""
@author: xiongbiao
@date: 2021-05-14 21:35
"""
'''
如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
n >= 3
对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
给定一个严格递增的正整数数组形成序列，找到 A 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
'''
class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import defaultdict
        mapping = {x: i for i, x in enumerate(arr)}
        dis = defaultdict(lambda: 2)

        ans = 0
        for k, a in enumerate(arr):
            for j in range(k):
                i = mapping.get(a - arr[j], None)
                if i is not None and i < j:
                    val = dis[j, k] = dis[i, j] + 1
                    ans = max(ans, val)

        return ans if ans >= 3 else 0