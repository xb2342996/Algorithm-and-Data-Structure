## written by xiongbiao
## date 2020-6-6

'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        cols, rows = len(triangle[-1]), len(triangle)
        print(cols, rows)

        if rows == 1:
            return triangle[0][0]

        if rows == 2:
            return triangle[0][0] + min(triangle[1][0], triangle[1][1])

        dp = [[0] * cols for _ in range(rows)]

        dp[0][0] = triangle[0][0]

        for i in range(rows):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

        for i in range(2, rows):
            for j in range(1, i - 1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

        return min(dp[-1])

print(Solution().minimumTotal([[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],[-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],[-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]))