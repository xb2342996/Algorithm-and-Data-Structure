"""
@author: xiongbiao
@date: 2021-05-02 21:43
"""

'''
假设你有一个长度为 n 的数组，初始情况下所有的数字均为 0，你将会被给出 k​​​​​​​ 个更新的操作。
其中，每个操作会被表示为一个三元组：[startIndex, endIndex, inc]，你需要将子数组 A[startIndex ... endIndex]（包括 startIndex 和 endIndex）增加 inc。
请你返回 k 次操作后的数组。
'''
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        # ans = [0] * length
        # for l, r, inc in updates:
        #     p = [0] * length
        #     for m in range(l, r + 1):
        #         p[m] = inc
        #     ans = list(map(lambda x, y: x + y, ans, p))
        # return ans

        ans = [0] * length
        for l, r, i in updates:
            ans[l] += i
            if r + 1 < length:
                ans[r + 1] -= i

        for i in range(1, length):
            ans[i] += ans[i - 1]
        return ans

print(Solution().getModifiedArray(5, [[1,3,2],[2,4,3],[0,2,-2]]))