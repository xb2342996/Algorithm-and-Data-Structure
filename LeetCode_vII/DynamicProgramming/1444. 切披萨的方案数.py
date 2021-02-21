"""
@author: xiongbiao
@date: 2021-02-12
"""


'''
给你一个 rows x cols 大小的矩形披萨和一个整数 k ，矩形包含两种字符： 'A' （表示苹果）和 '.' （表示空白格子）。你需要切披萨 k-1 次，得到 k 块披萨并送给别人。
切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，将披萨一分为二。如果垂直地切披萨，那么需要把左边的部分送给一个人，如果水平地切，那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的一块送给最后一个人。
请你返回确保每一块披萨包含 至少 一个苹果的切披萨方案数。由于答案可能是个很大的数字，请你返回它对 10^9 + 7 取余的结果。
'''

class Solution(object):
    def ways(self, pizza, k):
        """
        :type pizza: List[str]
        :type k: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        row = len(pizza)
        column = len(pizza[0])
        rest = [[0] * (column + 1) for _ in range(row + 1)]
        for i in range(row-1, -1, -1):
            for j in range(column-1, -1, -1):
                cur = 1 if pizza[i][j] == 'A' else 0
                rest[i][j] = rest[i+1][j] + rest[i][j+1] - rest[i+1][j+1] + cur

        dp = [[[0] * column for _ in range(row)] for _ in range(k)]
        dp[0][0][0] = 1
        for n in range(1, k):
            for i in range(row):
                for j in range(column):
                    count = 0
                    for p in range(0, i):
                        if self.hasA(p, j, i, j, rest):
                            count += dp[n-1][p][j]
                            count %= mod

                    for q in range(0, j):
                        if self.hasA(i, q, i, j, rest):
                            count += dp[n-1][i][q]
                            count %= mod

                    dp[n][i][j] = count

        ans = 0
        for i in range(row):
            for j in range(column):
                ans += dp[k-1][i][j]
                ans %= mod
        return ans


    def hasA(self, m, n, i, j, rest):
        return rest[i][j] - rest[m][n] != 0 and rest[i][j] != 0

print(Solution().ways(pizza = ["A..","A..","..."], k = 1))