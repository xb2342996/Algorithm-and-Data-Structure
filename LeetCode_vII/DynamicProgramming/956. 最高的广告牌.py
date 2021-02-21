"""
@author: xiongbiao
@date: 2021-02-14
"""
'''
你正在安装一个广告牌，并希望它高度最大。这块广告牌将有两个钢制支架，两边各一个。每个钢支架的高度必须相等。
你有一堆可以焊接在一起的钢筋 rods。举个例子，如果钢筋的长度为 1、2 和 3，则可以将它们焊接在一起形成长度为 6 的支架。
返回广告牌的最大可能安装高度。如果没法安装广告牌，请返回 0。
'''

class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        dp = {0: 0}
        for i in rods:
            dp_ = dp.copy()
            for k, v in list(dp_.items()):
                dp[k + i] = max(dp.get(k + i, 0), dp_[k] + i)
                dp[k - i] = max(dp.get(k - i, 0), dp_[k])
                # print(dp)
        return dp[0]

Solution().tallestBillboard([1, 2, 3, 4, 5])