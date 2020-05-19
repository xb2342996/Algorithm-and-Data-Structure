# written by xiongbiao
# date: 2020-5-18

class List(object):
    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size
    '''
    添加一个值在链表尾部，复用插入节点在某个位置
    '''
    def add_value(self, value):
        self.add_value_at(value, self._size)

    def add_value_at(self, value, index):
        raise NotImplementedError

    def remove_value_at(self, index):
        raise NotImplementedError

    def remove_value(self, value):
        raise NotImplementedError

    def value_at(self, value):
        raise NotImplementedError

    def get_value(self, index):
        raise NotImplementedError

    def set_value(self, index, value):
        raise NotImplementedError

    def contains_value(self, value):
        raise NotImplementedError

    def _get_node(self, index):
        raise NotImplementedError

    def _range_check(self, index):
        if index >= self._size or index < 0:
            raise IndexError('Index is out of range, Index must be in [0, ' + str(self._size) + ')')

    def _range_check_for_add(self, index):
        if index > self._size or index < 0:
            raise IndexError('Index is out of range, Index must be in [0, ' + str(self._size) + ']')

