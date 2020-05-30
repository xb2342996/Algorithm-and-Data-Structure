## written by xiongbiao
## date 2020-5-30

'''
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
'''


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        num = list(num)

        stack = []
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)

        if k:
            stack = stack[:-k]

        return ''.join(stack).lstrip('0') or 0

print(Solution().removeKdigits('10', 2))