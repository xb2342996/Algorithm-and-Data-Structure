"""
@author: xiongbiao
@date: 2021-03-07 16:09
"""

'''
你需要制定一份 d 天的工作计划表。工作之间存在依赖，要想执行第 i 项工作，你必须完成全部 j 项工作（ 0 <= j < i）。
你每天 至少 需要完成一项任务。工作计划的总难度是这 d 天每一天的难度之和，而一天的工作难度是当天应该完成工作的最大难度。
给你一个整数数组 jobDifficulty 和一个整数 d，分别代表工作难度和需要计划的天数。第 i 项工作的难度是 jobDifficulty[i]。
返回整个工作计划的 最小难度 。如果无法制定工作计划，则返回 -1 。
'''

class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        n = len(jobDifficulty)
        if n < d:
            return -1

        dp = [[float('inf')] * n  for _ in range(d)]
        v = jobDifficulty[0]
        for i in range(n):
            v = max(v, jobDifficulty[i])
            dp[0][i] = v

        for i in range(1, d):
            for j in range(i, n):
                dp[i][j] = dp[i-1][j-1] + jobDifficulty[j]
                v = jobDifficulty[j]
                for k in range(j, i-1, -1):
                    v = max(jobDifficulty[k-1], v)
                    dp[i][j] = min(dp[i][j], dp[i-1][k-1] + v)
        return dp[d-1][n-1]

print(Solution().minDifficulty(jobDifficulty = [11,111,22,222,33,333,44,444], d = 6))