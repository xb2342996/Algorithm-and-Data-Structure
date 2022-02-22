"""
@author: xiongbiao
@date: 2021-05-03 21:11
"""
'''
给定一幅由黑色像素和白色像素组成的图像， 与一个正整数N, 找到位于某行 R 和某列 C 中且符合下列规则的黑色像素的数量:
行R 和列C都恰好包括N个黑色像素。
列C中所有黑色像素所在的行必须和行R完全相同。
图像由一个由‘B’和‘W’组成二维字符数组表示, ‘B’和‘W’分别代表黑色像素和白色像素。
'''
from collections import defaultdict


class Solution(object):
    def findBlackPixel(self, picture, target):
        """
        :type picture: List[List[str]]
        :type target: int
        :rtype: int
        """
        row, col = len(picture), len(picture[0])
        row_dict = defaultdict(int)
        col_dict = defaultdict(int)
        row_count = defaultdict(int)
        for line in picture:
            s = ''.join(line)
            row_count[s] += 1
            if s not in row_dict:
                count = 0
                for c in range(col):
                    if line[c] == 'B':
                        count += 1
                row_dict[s] = count

        for r in range(row):
            for c in range(col):
                if picture[r][c] == 'B':
                    col_dict[c] += 1

        ans = 0
        for s, times in row_count.items():
            if times == target:
                for j in range(col):
                    if s[j] == 'B' and row_dict[s] == target and col_dict[j] == target:
                        ans += 1
        return ans * target



print(Solution().findBlackPixel([['W', 'B', 'W', 'B', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'B', 'W'],
 ['W', 'W', 'B', 'W', 'B', 'W']], 3))
