## written by xiongbiao
## date 2020-5-31
'''
使用队列实现栈的下列操作：
push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
'''
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """

        self.q.append(x)
        size = len(self.q)
        while size != 1:
            self.q.append(self.q.pop(0))
            size -= 1


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.pop(0)


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q[0]


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q) == 0

s = MyStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)