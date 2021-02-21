"""
@author: xiongbiao
@date: 2021-02-14
"""
'''
你打算利用空闲时间来做兼职工作赚些零花钱。
这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。
给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。
注意，时间上出现重叠的 2 份工作不能同时进行。
如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。
'''

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[1])
        dp = [0] * (jobs[-1][1] + 1)
        curr = 0
        for job in jobs:
            j = curr + 1
            while j <= job[1]:
                dp[j] = dp[j-1]
                j += 1
            dp[job[1]] = max(dp[job[0]] + job[2], dp[job[1]])
            curr = job[1]

        return dp[-1]

print(Solution().jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))