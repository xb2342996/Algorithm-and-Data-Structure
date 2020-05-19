## written by xiongbiao
## date 2020-5-19

'''
队列思路
1. 线性结构
2. 顺序相同
'''
class Queue(object):
    def __init__(self):
        self.__queue = []

    def clear(self):
        self.__queue = []

    def size(self):
        return len(self.__queue)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, value):
        self.__queue.append(value)

    def dequeue(self):
        if self.size() == 0:
            raise IndexError('queue is empty, can not pop value')
        return self.__queue.pop(0)

    def front(self):
        return self.__queue[0]

    def __repr__(self):
        s = 'Queue: ['
        for i, n in enumerate(self.__queue):
            if i == 0:
                s += '{}'.format(n)
            else:
                s += ', {}'.format(n)
        s += ']'
        return s
#
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(5)
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# print(queue)