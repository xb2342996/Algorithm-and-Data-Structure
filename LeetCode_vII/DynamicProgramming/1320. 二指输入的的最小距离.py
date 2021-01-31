"""
@author: xiongbiao
@date: 2021-01-24 15:35
"""

'''
二指输入法定制键盘在 XY 平面上的布局如上图所示，其中每个大写英文字母都位于某个坐标处，例如字母 A 位于坐标 (0,0)，字母 B 位于坐标 (0,1)，字母 P 位于坐标 (2,3) 且字母 Z 位于坐标 (4,1)。
给你一个待输入字符串 word，请你计算并返回在仅使用两根手指的情况下，键入该字符串需要的最小移动总距离。坐标 (x1,y1) 和 (x2,y2) 之间的距离是 |x1 - x2| + |y1 - y2|。 
注意，两根手指的起始位置是零代价的，不计入移动总距离。你的两根手指的起始位置也不必从首字母或者前两个字母开始。
'''
class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        def distance(i, j):
            a = i // 6
            b = i % 6
            c = j // 6
            d = j % 6
            return abs(a-c) + abs(b-d)

        def index(k):
            return ord(word[k]) - 65

        dp = [[0] * 26] + [[float('inf')] * 26 for _ in range(len(word)-1)]
        for i in range(1, len(word)):
            prev = index(i - 1)
            cur = index(i)
            d = distance(prev, cur)
            for j in range(26):
                dp[i][j] = min(dp[i][j], dp[i-1][j] + d)
                if prev == j:
                    for k in range(26):
                        ds = distance(k, cur)
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + ds)

        return int(min(dp[len(word) - 1]))



print(Solution().minimumDistance('CAKE'))