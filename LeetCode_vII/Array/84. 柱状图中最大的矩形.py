## written by xiongbiao
## date 2020-5-29
'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
'''

class Solution(object):

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0

        if len(heights) == 1:
            return heights[0]

        stack = []
        stack.append(-1)
        maxArea = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                index = stack.pop()
                maxArea = max(maxArea, heights[index] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            maxArea = max(maxArea, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return maxArea
    '''
    二分法 求出最小的柱子高度计算最小高度左侧，右侧，和整体高度的最大值
    时间复杂度O（NlogN）最坏情况下O（N^2)（有序高度） 空间复杂度O（N）
    '''
    # def largestRectangleArea(self, heights):
    #     """
    #     :type heights: List[int]
    #     :rtype: int
    #     """
    #     if len(heights) == 0:
    #         return 0
    #
    #     if len(heights) == 1:
    #         return heights[0]
    #
    #     return self.calculateArea(0, len(heights) - 1, heights)
    #
    # def calculateArea(self, start, end, heights):
    #     if start > end:
    #         return 0
    #     minIndex = start
    #     for i in range(start, end + 1):
    #         if heights[i] < heights[minIndex]:
    #             minIndex = i
    #
    #     return max(self.calculateArea(start, minIndex - 1, heights), self.calculateArea(minIndex + 1, end, heights), (end + 1 - start) * heights[minIndex])


    '''
    暴力法优化：遍历所有的柱子，遍历过程中记录遍历过的高度的最小值，计算面积
    时间复杂度O（N^2) 空间复杂度O（1）
    '''
    # def largestRectangleArea(self, heights):
    #     """
    #     :type heights: List[int]
    #     :rtype: int
    #     """
    #     if len(heights) == 0:
    #         return 0
    #
    #     if len(heights) == 1:
    #         return heights[0]
    #
    #     h = len(heights)
    #     maxArea = 0
    #     minHeight = float('inf')
    #     for i in range(h):
    #         for j in range(i, h):
    #             minHeight = min(minHeight, heights[j])
    #             maxArea = max(minHeight * (j - i + 1), maxArea)
    #     return maxArea
    '''
    暴力法：遍历所有的柱子，寻找柱子之间的最矮高度，计算面积
    时间复杂度O（N^3) 空间复杂度O（1）
    '''
    # def largestRectangleArea(self, heights):
    #     """
    #     :type heights: List[int]
    #     :rtype: int
    #     """
    #     if len(heights) == 0:
    #         return 0
    #
    #     if len(heights) == 1:
    #         return heights[0]
    #
    #     h = len(heights)
    #     maxArea = 0
    #     for i in range(h):
    #         for j in range(i, h):
    #             minHeight = float('inf')
    #             for k in range(i, j + 1):
    #                 minHeight = min(minHeight, heights[k])
    #             maxArea = max(minHeight * (j - i + 1), maxArea)
    #     return maxArea

print(Solution().largestRectangleArea([1,1,1,1,1,1,1,1,1,6,6]))
