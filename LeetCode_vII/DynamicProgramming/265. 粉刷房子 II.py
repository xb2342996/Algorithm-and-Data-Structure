'''
假如有一排房子，共 n 个，每个房子可以被粉刷成 k 种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x k 的矩阵来表示的。
例如，costs[0][0] 表示第 0 号房子粉刷成 0 号颜色的成本花费；costs[1][2] 表示第 1 号房子粉刷成 2 号颜色的成本花费，以此类推。请你计算出粉刷完所有房子最少的花费成本。
注意：
所有花费均为正整数。
示例：
输入: [[1,5,3],[2,9,4]]
输出: 5
解释: 将 0 号房子粉刷成 0 号颜色，1 号房子粉刷成 2 号颜色。最少花费: 1 + 4 = 5;
     或者将 0 号房子粉刷成 2 号颜色，1 号房子粉刷成 0 号颜色。最少花费: 3 + 2 = 5.
进阶：
您能否在 O(nk) 的时间复杂度下解决此问题？
'''
class Solution(object):
    '''
    动态规划，遍历前一个房子的颜色，选择不等于当前颜色的且花费最小的于当前颜色花费相加，直到所有房子都计算完成，时间复杂度O(NK^2)
    优化：如果前面所有房子花费最小的房子颜色与当前选择的颜色一样，则选择第二小花费的颜色与当前颜色花费相加，否则前一个房子最小花费颜色与当前颜色相加，
         所以，需要前一个房子的最小花费和第二小花费，并记录最小花费颜色位置。时间复杂度O（NK）
    '''
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
        colors = len(costs[0])
        houses = len(costs)
        dp = [[0] * colors for _ in range(0, houses)]

        minColor = -1
        minCost = 0
        minSecondCost = 0
        for i in range(0, houses):
            tmpMinColor = -1
            tmpMinCost = float('inf')
            tmpMinSecondCost = float('inf')
            for j in range(0, colors):
                if j == minColor:
                    dp[i][j] = minSecondCost + costs[i][j]
                else:
                    dp[i][j] = minCost + costs[i][j]

                if dp[i][j] < tmpMinCost:
                    tmpMinSecondCost = tmpMinCost
                    tmpMinCost = dp[i][j]
                    tmpMinColor = j
                elif dp[i][j] < tmpMinSecondCost:
                    tmpMinSecondCost = dp[i][j]
            minColor = tmpMinColor
            minCost = tmpMinCost
            minSecondCost = tmpMinSecondCost

        return minCost


print(Solution().minCostII([[1, 5, 3], [2, 9, 4]]))