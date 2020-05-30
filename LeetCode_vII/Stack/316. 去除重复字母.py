## written by xiongbiao
## date 2020-5-29

'''
给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。
需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
'''
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last = {}
        for i, n in enumerate(s):
            last[n] = i

        stack = []
        seen = set()
        for i, n in enumerate(s):
            if n not in seen:
                while len(stack) > 0 and stack[-1] > n and i < last[stack[-1]]:
                    seen.discard(stack.pop())
                stack.append(n)
                seen.add(n)

        return ''.join(stack)

Solution().removeDuplicateLetters('cbacdcbc')