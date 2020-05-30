## written by xiongbiao
## date 2020-5-30
'''
实现 FreqStack，模拟类似栈的数据结构的操作的一个类。
FreqStack 有两个函数：
push(int x)，将整数 x 推入栈中。
pop()，它移除并返回栈中出现最频繁的元素。如果最频繁的元素不只一个，则移除并返回最接近栈顶的元素。
'''


class FreqStack(object):

    def __init__(self):
        from collections import Counter, defaultdict
        self.freq = Counter()
        self.stack = defaultdict(list)
        self.max_freq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        f = self.freq[x] + 1
        self.freq[x] = f
        if self.max_freq < f:
            self.max_freq = f
        self.stack[f].append(x)

    def pop(self):
        """
        :rtype: int
        """
        pop_elem = self.stack[self.max_freq].pop()
        self.freq[pop_elem] -= 1
        if not self.stack[self.max_freq]:
            self.max_freq -= 1

        return pop_elem
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)

print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())