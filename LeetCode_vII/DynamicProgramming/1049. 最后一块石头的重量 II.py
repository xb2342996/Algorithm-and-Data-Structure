"""
@author: xiongbiao
@date: 2021-01-11 23:10
"""
'''
有一堆石头，每块石头的重量都是正整数。
每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。
'''
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total = sum(stones)
        weight = (total // 2) + 1
        dp = [[0] * weight for _ in range(len(stones))]
        for i in range(len(stones)):
            for j in range(weight):
                if stones[i] > j:
                    if i == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i-1][j]
                else:
                    if i == 0:
                        dp[i][j] = stones[i]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i]] + stones[i])
        return total - (dp[-1][-1] * 2)


print(Solution().lastStoneWeightII([2,7,4,1,8,1]))