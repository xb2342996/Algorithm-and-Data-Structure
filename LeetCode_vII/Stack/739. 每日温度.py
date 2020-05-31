## written by xiongbiao
## date 2020-5-31
'''
根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。
如果之后都不会升高，请在该位置用 0 来代替。
'''
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []
        for i in range(len(T))[::-1]:
            while stack and T[stack[-1]] < T[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i

            stack.append(i)
        print(ans)
        return ans
    # def dailyTemperatures(self, T):
    #     """
    #     :type T: List[int]
    #     :rtype: List[int]
    #     """
    #     ans = [0] * len(T)
    #     print(ans)
    #     stack = []
    #     for i in range(len(T)):
    #         while stack and T[stack[-1]] < T[i]:
    #             index = stack.pop()
    #             ans[index] = i - index
    #
    #         stack.append(i)
    #
    #     return ans

Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
