## written by xiongbiao
## date 2020-5-29

'''
实现一个基本的计算器来计算简单的表达式字符串。
表达式字符串可以包含左括号 ( 和右括号 )，加号 + 和减号 -，非负 整数和空格 。
表达式字符串只包含非负整数， +, -, *, / 操作符，左括号 ( ，右括号 )和空格 。整数除法需要向下截断。
'''


class Solution(object):
    '''
    将问题拆解成子问题
    1，读取无空格字符
    2. 添加加减法
    3. 添加乘除法
    4。添加处理括号的功能
    没当读到一个操作符，上一次读到的操作符已经被记录，计算上一次读到的操作符与数字的运算
    如果是+：压栈+数字
    如果是-：压栈-数字
    如果是*|/: 上一次压入栈的数字与刚读取的数字的积或商
    如果是（：递归计算（）内的内容
    如果是）：结束循环，计算站内的和
    '''
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def helper(s):
            stack = []
            num = 0
            sign = '+'
            while len(s) > 0:
                n = s.pop(0)
                if n.isdigit():
                    num = 10 * num + int(n)
                if n == '(':
                    num = helper(s)
                if (not n.isdigit() and n != ' ') or len(s) == 0:
                    if sign is '+':
                        stack.append(+num)
                    elif sign is '-':
                        stack.append(-num)
                    elif sign is '*':
                        stack.append(num * stack.pop())
                    elif sign is '/':
                        stack.append(int(stack.pop() / float(num)))
                    sign = n
                    num = 0
                if n == ')':
                    break

            return sum(stack)

        return helper(list(s))


print(Solution().calculate('5-3/2'))