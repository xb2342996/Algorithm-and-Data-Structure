## written by xiongbiao
## date 2020-5-19

'''
栈的思路:
1. 线性结构
2. 输入顺序与输出顺序相反
3. 多个栈存储状态
'''
class Stack:
    def __init__(self):
        self.__stack = []

    def clear(self):
        self.__stack = []

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.__stack)

    def pop(self):
        if self.size() == 0:
            raise IndexError('stack is empty, can not pop value')
        return self.__stack.pop()

    def push(self, value):
        self.__stack.append(value)

    def top(self):
        return self.__stack[self.size() - 1]

    def __repr__(self):
        s = 'Stack: ['
        for i, n in enumerate(self.__stack):
            if i == 0:
                s += '{}'.format(n)
            else:
                s += ', {}'.format(n)
        s += ']'
        return s

stack = Stack()
stack.push(12)
stack.push(22)
stack.push(32)
stack.push(42)
stack.push(52)
stack.pop()
stack.pop()
stack.pop()
print(stack.top())
stack.clear()
print(stack)