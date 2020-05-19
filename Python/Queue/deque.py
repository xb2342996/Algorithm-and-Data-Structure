## written by xiongbiao
## date 2020-5-19

class Deque(object):
    def __init__(self):
        self.__queue = []

    def size(self):
        return len(self.__queue)

    def is_empty(self):
        return self.size() == 0

    def clear(self):
        self.__queue = []

    def enqueue_rear(self, value):
        self.__queue.append(value)

    def enqueue_front(self, value):
        self.__queue.insert(0, value)

    def dequeue_rear(self):
        if self.size() == 0:
            raise IndexError('deque is empty, can not dequeue value')
        self.__queue.pop()

    def dequeue_front(self):
        if self.size() == 0:
            raise IndexError('deque is empty, can not dequeue value')
        self.__queue.pop(0)

    def rear(self):
        return self.__queue[self.size() - 1]

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

deque = Deque()
deque.enqueue_front(1)
deque.enqueue_front(2)
deque.enqueue_front(13)
deque.enqueue_front(14)
deque.enqueue_rear(15)
deque.enqueue_rear(5)
deque.enqueue_rear(25)
print(deque.rear())
print(deque.front())
for _ in range(3):
    deque.dequeue_front()
    deque.dequeue_rear()
    print(deque)
print(deque.rear())
print(deque.front())
print(deque.is_empty())