"""
@author: xiongbiao
@date: 2022-02-23 23:09
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        stack = []
        num = 0
        sign = '+'
        for i, c in enumerate(s):
            if c != ' ' and c.isdigit():
                num = num * 10 + int(c)
            if c in '+-*/' or i == size - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = c
        return sum(stack)

print(Solution().calculate('14 - 3 / 2'))