## written by xiongbiao
## date 2020-5-30
'''
给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
'''
class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        size = len(hours)
        score = [1] * size
        for i in range(size):
            if hours[i] <= 8:
                score[i] = -1

        sum = 0
        prefix = []
        for s in score:
            prefix.append(sum)
            sum += s
        prefix.append(sum)

        stack = []
        for i in range(len(prefix)):
            if len(stack) == 0 or prefix[i] < prefix[stack[-1]]:
                stack.append(i)

        # print(stack)
        # print(prefix)
        ans = 0
        for i in range(len(prefix))[::-1]:
            while len(stack) > 0 and prefix[i] > prefix[stack[-1]]:
                ans = max(i - stack[-1], ans)
                stack.pop()
        return ans


print(Solution().longestWPI([9,9,6,0,6,6,9]))

