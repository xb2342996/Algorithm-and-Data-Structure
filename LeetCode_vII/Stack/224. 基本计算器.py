## written by xiongbiao
## date 2020-5-29

'''
实现一个基本的计算器来计算一个简单的字符串表达式的值。
字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。
'''


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        num = 0
        sign = 1
        stack = []
        ans = 0
        for n in s:
            if n.isdigit():
                num = num * 10 + int(n)

            elif n == '+':
                ans += sign * num
                num = 0
                sign = 1
            elif n == '-':
                ans += sign * num
                num = 0
                sign = -1
            elif n == '(':
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
            elif n == ')':
                ans += sign * num
                ans *= stack.pop()
                ans += stack.pop()
                num = 0

        return ans + sign * num

print(Solution().calculate("2 - 1 + 1"))
