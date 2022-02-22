"""
@author: xiongbiao
@date: 2021-06-06 22:50
"""
'''
给你两个长度相同的字符串，s 和 t。
将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。
用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。
如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。
如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。
'''

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        # length = len(s)
        # left, cost = 0, 0
        # for right in range(length):
        #     cost += abs(ord(s[right]) - ord(t[right]))
        #     if cost > maxCost:
        #         cost -= abs(ord(s[left]) - ord(t[left]))
        #         left += 1
        #
        # return length - left

        length = len(s)
        diff = [abs(ord(s[i]) - ord(t[i])) for i in range(length)]

        n, cost, left = 0, 0, 0
        ans = 0
        while n < length:
            cost += diff[n]
            while cost > maxCost:
                cost -= diff[left]
                left += 1
            ans = max(ans, n - left + 1)
            n += 1
        return ans



print(Solution().equalSubstring('aaaa', 'aaaz', 24))