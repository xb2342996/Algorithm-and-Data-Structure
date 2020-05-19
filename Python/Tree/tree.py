## written by xiongbiao
## date 2020-5-19

from Queue.queue import Queue

class Node(object):
    def __init__(self, value=None, parent=None):
        self.left = None
        self.right = None
        self.value = value
        self.parent = parent

    def is_leaf(self):
        return self.left is None and self.right is None

class BinaryTree(object):
    def __init__(self):
        self._root = None
        self._size = 0
        self._height = 0

    def clear(self):
        self._root = None
        self._size = 0

    def height(self):
        return self.__height(self._root)

    def __height(self, node):
        if node is None:
            return 0
        return 1 + max(self.__height(node.left), self.__height(node.right))

    def width(self):
        return 2 ** (self.height() - 1)

    def size(self):
        return self.size()

    def inorder_traversal(self, type='recursive'):
        assert type in ['recursive', 'linear']
        nodes = []
        if self._root is None:
            return nodes

        if type == 'recursive':
            self._inorder_r(self._root, nodes)
        else:
            self._inorder_l(self._root, nodes)

        return nodes

    def _inorder_r(self, node, nodes):
        if node is None:
            return

        self._inorder_r(node.left, nodes)
        nodes.append(node.value)
        self._inorder_r(node.right, nodes)

    def _inorder_l(self, node, nodes):
        pass


    def preorder_traversal(self, type='recursive'):
        assert type in ['recursive', 'linear']
        nodes = []
        if self._root is None:
            return nodes

        if type == 'recursive':
            self._preorder_r(self._root, nodes)
        else:
            self._preorder_l(self._root, nodes)

        return nodes

    def _preorder_r(self, node, nodes):
        if node is None:
            return

        nodes.append(node.value)
        self._preorder_r(node.left, nodes)
        self._preorder_r(node.right, nodes)

    def _preorder_l(self, node, nodes):
        pass

    def postorder_traversal(self, type='recursive'):
        assert type in ['recursive', 'linear']
        nodes = []
        if self._root is None:
            return nodes

        if type == 'recursive':
            self._postorder_r(self._root, nodes)
        else:
            self._postorder_l(self._root, nodes)

        return nodes

    def _postorder_r(self, node, nodes):
        if node is None:
            return

        self._postorder_r(node.left, nodes)
        self._postorder_r(node.right, nodes)
        nodes.append(node.value)

    def _postorder_l(self, node, nodes):
        pass


    def level_order_traversal(self):
        traversal = []
        if self._root is None:
            return traversal

        queue = Queue()
        queue.enqueue(self._root)

        while not queue.is_empty():
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

            traversal.append(node.value)

        return traversal


    def reverse(self):
        if self._root is None:
            return
        self._reverse(self._root)

    def _reverse(self, node):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        self._reverse(node.left)
        self._reverse(node.right)

    def is_empty(self):
        return self.size() == 0

    def is_complete(self):
        if self._root is None:
            return False

        node = self._root
        queue = Queue()
        queue.enqueue(node)
        leaf = False
        while not queue.is_empty():
            node = queue.dequeue()
            if leaf and not node.is_leaf():
                return False
            if node.left and node.right:
                queue.enqueue(node.left)
                queue.enqueue(node.right)
            else:
                leaf = True
                if node.left:
                    queue.enqueue(node.left)
        return True


    def predecessor(self, node):
        if node is None:
            return
        p = node.left
        if p:
            while p.right:
                p = p.right
            return p

        while node.parent and node.parent.left == node:
            node = node.parent
        return node.parent


    def successor(self, node):
        if node is None:
            return

        p = node.right
        if p:
            while p.left:
                p = p.left
            return p

        while node.parent and node.parent.right == node:
            node = node.parent
        return node.parent

    def print(self):
        levels = {}
        queue = Queue()
        queue.enqueue(self._root)
        level = 0
        level_list = []
        count = 1
        while not queue.is_empty() and level < self.height():

            node = queue.dequeue()
            level_list.append(node.value)
            count -= 1

            if node.left:
                queue.enqueue(node.left)
            else:
                queue.enqueue(Node())
            if node.right:
                queue.enqueue(node.right)
            else:
                queue.enqueue(Node())

            if count == 0:
                count = queue.size()
                levels[level] = level_list
                level_list = []
                level += 1

        for key, value in levels.items():

            for v in value:
                if v is None:
                    print('N', end=' ')
                else:
                    print(v, end=' ')
            print()

