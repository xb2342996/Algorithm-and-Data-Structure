## written by xiongbiao
## date 2020-5-30
'''
根据逆波兰表示法，求表达式的值。
有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        signs = '+-*/'
        stack = []
        while tokens:
            s = tokens.pop(0)
            if s in signs:
                n1 = stack.pop()
                n2 = stack.pop()
                if s == '+':
                    stack.append(n1 + n2)
                elif s == '-':
                    stack.append(n2 - n1)
                elif s == '*':
                    stack.append(n1 * n2)
                elif s == '/':
                    stack.append(int(n2 / n1))
            else:
                stack.append(int(s))
            print(stack)
        return stack[0]

# print(Solution().evalRPN(["10", "6", "Total 9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
import math
print(math.ceil(6 / (-132)))