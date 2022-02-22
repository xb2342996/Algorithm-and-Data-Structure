"""
@author: xiongbiao
@date: 2022-02-20 22:59
"""

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        ans, count = 0, 0
        left, right = 0, 0
        size = len(s)
        q = dict()
        q[s[left]] = 0
        while right < size:
            if s[right] in q.keys():
                q[s[right]] = right
                right += 1
            elif len(q.keys()) < 2:
                q[s[right]] = right
                right += 1
            else:
                v = min(q.values())
                q.pop(s[v])
                left = v + 1
            count = right - left
            ans = max(count, ans)
            # print(q.items(), left, right, s[left: right])
        return ans

print(Solution().lengthOfLongestSubstringTwoDistinct('ccaabbb'))