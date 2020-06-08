## written by xiongbiao
## date 2020-6-8

'''
在计算机界中，我们总是追求用有限的资源获取最大的收益。
现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。
你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。
'''

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for s in strs:
            num_1 = s.count('1')
            num_0 = s.count('0')
            for i in range(num_1, n + 1)[::-1]:
                for j in range(num_0, m + 1)[::-1]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i-num_1][j-num_0])
            print(dp)
        return dp[-1][-1]

print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))