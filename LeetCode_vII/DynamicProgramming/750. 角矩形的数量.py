## written by xiongbiao
## date 2020-6-5

'''
给定一个只包含 0 和 1 的网格，找出其中角矩形的数量。
'''

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        cols = len(grid[0])
        rows = len(grid)
        ans = 0
        for i in range(cols):
            for j in range(i, cols):
                count = 0
                for k in range(rows):
                    if grid[i][k] == 1 and grid[j][k] == 1:
                        count += 1

                ans += (count * (count - 1)) >> 1

        return ans