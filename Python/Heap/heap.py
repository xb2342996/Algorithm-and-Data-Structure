# written by xiongbiao
# date 2020-5-20


class BinaryHeap():
    DEFAULT_CAPACITY = 10
    def __init__(self, nums=None):
        if nums:
            self.__nums = nums
            self.__size = len(nums)
            self.__heapify()
        else:
            self.__nums = [None] * BinaryHeap.DEFAULT_CAPACITY
            self.__size = 0

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def clear(self):
        for i in range(self.__size):
            self.__nums[i] = None
        self.__size = 0
    '''
    向堆中添加元素，动态扩容，将添加的元素上溢
    '''
    def add(self, value):
        self.__check_null_value(value)
        self.__ensure_capacity()
        self.__nums[self.__size] = value
        self.__size += 1
        self.__sift_up(self.__size - 1)

    '''
    获取堆头结点
    '''
    def get(self):
        self.__check_empty()
        return self.__nums[0]

    '''
    删除对顶元素，用对中最后一个元素替代堆顶元素，将堆顶下溢
    '''
    def remove(self):
        self.__check_empty()
        self.__nums[0] = self.__nums[self.__size - 1]
        self.__nums[self.__size - 1] = None
        self.__size -= 1
        self.__sift_down(0)

    '''
    替代堆顶元素，若堆不空，堆顶下溢
    '''
    def replace(self, value):
        self.__check_null_value(value)
        old = None
        if self.__size == 0:
            self.__nums[0] = value
            self.__size += 1
        else:
            old = self.__nums[0]
            self.__nums[0] = value
            self.__sift_down(0)
        return old

    '''
    上溢，对于符合堆要求的子节点与父节点，将子节点的值赋给父节点，父节点变为子节点，继续向上找，直到没有父节点或符合堆的要求
    '''
    def __sift_up(self, index):
        node = self.__nums[index]
        while index > 0:
            parent = (index - 1) >> 1
            if self.__nums[parent] > node:
                break
            self.__nums[index] = self.__nums[parent]
            index = parent

        self.__nums[index] = node

    '''
    下溢，下溢操作只需要找到叶子节点的父节点即可结束，找到下溢节点的左右节点，选择左右节点中值大的节点并赋给父节点，直到堆符合要求
    '''
    def __sift_down(self, index):
        node = self.__nums[index]
        while index < (self.__size >> 1):
            left = (index << 1) + 1
            right = left + 1
            child = self.__nums[left]
            if right < self.__size and self.__nums[left] < self.__nums[right]:
                child = self.__nums[right]
                left = right

            if child < node:
                break
            self.__nums[index] = child
            index = left

        self.__nums[index] = node


    def __heapify(self):
        for i in range(self.__size >> 1)[::-1]:
            self.__sift_down(i)

    def __check_empty(self):
        if self.size() == 0:
            raise IndexError('Heap is empty')

    def __ensure_capacity(self):

        if self.__size + 1 < len(self.__nums):
            return

        size = len(self.__nums)
        new_size = (size >> 1) + size
        new_nums = [None] * new_size

        for i in range(self.__size):
            new_nums[i] = self.__nums[i]

        self.__nums = new_nums

    def __check_null_value(self, value):
        if value is None:
            raise ValueError('value must not be None')

    def show(self):
        print(self.__nums)

def test_func():
    nums = [51, 30, 39, 92, 74, 25, 16, 93]
    heap = BinaryHeap(nums)

    # for n in nums:
    #     heap.add(n)
    # heap.remove()
    # heap.remove()
    # heap.remove()
    # heap.remove()
    # heap.remove()
    # heap.remove()
    # heap.remove()
    # heap.remove()
    heap.show()

# test_func()