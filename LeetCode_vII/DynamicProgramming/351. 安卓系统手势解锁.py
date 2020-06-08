## written by xiongbiao
## date 2020-6-7
'''
我们都知道安卓有个手势解锁的界面，是一个 3 x 3 的点所绘制出来的网格。
给你两个整数，分别为 ​​m 和 n，其中 1 ≤ m ≤ n ≤ 9，那么请你统计一下有多少种解锁手势，是至少需要经过 m 个点，但是最多经过不超过 n 个点的。
'''
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.visited = [False] * 10
        self.cross = [[0] * 10 for _ in range(10)]
        self.cross[1][3] = self.cross[3][1] = 2
        self.cross[1][7] = self.cross[7][1] = 4
        self.cross[2][8] = self.cross[8][2] = self.cross[1][9] = self.cross[9][1] = 5
        self.cross[3][7] = self.cross[7][3] = self.cross[4][6] = self.cross[6][4] = 5
        self.cross[3][9] = self.cross[9][3] = 6
        self.cross[7][9] = self.cross[9][7] = 8

        ans = 0
        for i in range(m, n+1):
            ans += self.dfs(1, i-1) * 4
            ans += self.dfs(2, i-1) * 4
            ans += self.dfs(5, i-1)

        return ans

    def dfs(self, current, rest):
        if rest == 0:
            return 1
        res = 0
        self.visited[current] = True
        for i in range(1, 10):
            crossNum = self.cross[current][i]
            print(crossNum)
            if not self.visited[i] and (self.visited[crossNum] or crossNum == 0):
                res += self.dfs(i, rest - 1)

        self.visited[current] = False
        return res

print(Solution().numberOfPatterns(1,2))