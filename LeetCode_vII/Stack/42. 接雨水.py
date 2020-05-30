## written by xiongbiao
## date 2020-5-30
'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
'''
class Solution(object):
    '''
    记录每个位置的左边最大的柱子和右边最大的柱子的高度，找到2个高度中最小的减去当前的高度
    '''
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height) - 1
        leftMax = 0
        rightMax = [0] * len(height)
        ans = 0

        for i in range(1, length)[::-1]:
            rightMax[i] = max(rightMax[i+1], height[i + 1])

        for i in range(1, length):
            leftMax = max(leftMax, height[i - 1])
            minVal = min(leftMax, rightMax[i])
            if minVal <= height[i]:
                continue
            ans += minVal - height[i]
        return ans
    '''
    使用单调递减栈存放每个柱子，新的柱子大于栈顶，将栈顶出栈计算新柱子与栈顶元素的距离，计算栈顶与新柱子的最小高度-弹出栈的柱子，再乘以距离
    等于面积
    '''
    # def trap(self, height):
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #     if len(height) == 0:
    #         return 0
    #
    #     stack = []
    #     ans = 0
    #     for i, h in enumerate(height):
    #         while len(stack) > 0 and h > height[stack[-1]]:
    #             index = stack.pop()
    #             if not stack:
    #                 break
    #             distance = i - stack[-1] - 1
    #
    #             min_height = min(h, height[stack[-1]]) - height[index]
    #             ans += min_height * distance
    #
    #         stack.append(i)
    #
    #     return ans

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))

