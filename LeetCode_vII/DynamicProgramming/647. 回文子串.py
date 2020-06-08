## written by xiongbiao
## date 2020-6-7

'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
'''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = (len(s) << 1) + 1
        ans = 0

        for i in range(n):
            left = i >> 1
            right = left + i % 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                ans += 1

        return ans
print(Solution().countSubstrings('aba'))