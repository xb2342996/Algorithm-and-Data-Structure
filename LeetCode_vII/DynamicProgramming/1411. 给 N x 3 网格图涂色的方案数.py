"""
@author: xiongbiao
@date: 2021-01-24 21:21
"""

'''
你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜色不同）。
给你网格图的行数 n 。
请你返回给 grid 涂色的方案数。由于答案可能会非常大，请你返回答案对 10^9 + 7 取余的结果。
'''

class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        aba, abc = 6, 6
        for i in range(n - 1):
            aba, abc = (2 * abc + 3 * aba) % mod, (2 * aba + 2 * abc) % mod

        return (abc + aba) % mod

print(Solution().numOfWays(7))


