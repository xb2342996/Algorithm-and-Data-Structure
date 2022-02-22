"""
@author: xiongbiao
@date: 2022-01-19 22:23
"""

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = [0] * 121
        for a in ages:
            count[a] += 1

        prefix = [0] * 121
        for i in range(1, 121):
            prefix[i] = prefix[i-1] + count[i]

        ans = 0
        for a in range(15, 121):
            if count[a] > 0:
                bound = int(0.5 * a + 8)
                ans += (prefix[a] - prefix[bound - 1] - 1) * count[a]

        return ans


s = Solution().numFriendRequests([20,30,100,110,120])
print(s)