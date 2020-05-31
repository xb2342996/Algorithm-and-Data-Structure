## written by xiongbiao
## date 2020-5-31
'''
使用栈实现队列的下列操作：
push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
'''
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.top = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if not self.s1:
            self.top = x
        self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        print(self.s1, self.s2)
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.s2:
            return self.s2[-1]
        return self.top


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.s1) == 0 and len(self.s2) == 0

q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())
print(q.pop())