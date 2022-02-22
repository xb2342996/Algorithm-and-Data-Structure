"""
@author: xiongbiao
@date: 2022-02-21 22:53
"""

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import defaultdict
        l_s, l_t = len(s), len(t)
        if abs(l_s - l_t) > 1 or s == t:
            return False

        # if l_t > l_s:
        #     s, t = t, s

        diff = 0
        l, r = 0, 0
        while l < l_s and r < l_t:
            if diff > 1:
                return False
            if s[l] == t[r]:
                l += 1
                r += 1
            else:
                diff += 1
                if l_t > l_s:
                    r += 1
                elif l_t < l_s:
                    l += 1
                else:
                    l += 1
                    r += 1
        if diff > 1:
            return False
        if r + 1 < l_t or l + 1 < l_s:
            return False

        return True



print(Solution().isOneEditDistance('', 'y'))