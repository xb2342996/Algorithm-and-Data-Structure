
from Queue.queue import Queue

class Node(object):
    def __init__(self, string=None):
        self.btNode = None
        self.left = None
        self.right = None
        self.parent = None

        self.x = 0
        self.y = 0
        self.tree_height = 0


        if string is None:
            self.string = string
        else:
            self.string = 'none'

        if len(self.string) == 0:
            self.string = ' '
        else:
            self.string = string

        self.width = len(self.string)

    def top_lineX(self):
        delta = self.width

        if (delta % 2 == 0):
            delta -= 1
        delta >>= 1

        if (self.parent is not None) and (self == self.parent.left):
            return self.rightX() - 1 - delta
        else:
            return self.x +delta

    def rightX(self):
        return self.x + self.width

    def right_bound(self):
        if (self.right is None):
            return self.rightX()
        return self.right.top_lineX() + 1

    def left_bound(self):
        if (self.left is None):
            return self.x
        return self.left.top_lineX()

    def left_bound_length(self):
        return self.x - self.left_bound()

    def right_bound_length(self):
        return self.right_bound() - self.rightX()

    def left_bound_empty_length(self):
        return self.left_bound_length() - 1 - 1

    def right_bound_empty_length(self):
        return self.right_bound_length() - 1 - 1

    def treeHeight(self, node):
        if node is None:
            return 0

        if node.tree_height != 0:
            return node.tree_height

        node.tree_height = 1 + max(self.treeHeight(node.left), self.treeHeight(node.right))
        return node.tree_height

    def min_level_space_2_right(self, right):
        this_height = self.treeHeight(self)
        right_height = self.treeHeight(right)
        min_space = int('inf')
        for i in range(this_height):
            if i < right_height:
                space = right.levelInfo(i).leftX - self.levelInfo(i).rightX
                min_space = min(min_space, space)

        return min_space

    def levelInfo(self, level):
        if level < 0:
            return None
        levelY = self.y + level
        if level >= self.treeHeight(self):
            return None

        node_list = []
        queue = Queue()
        queue.enqueue(self)

        while not queue.is_empty():
            node = queue.dequeue()
            if levelY == node.y:
                node_list.append(node)
            elif node.y > levelY:
                break

            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)

        left = node_list[0]
        right = node_list[len(node_list) - 1]
        return LevelInfo(left, right)

    def translateX(self, deltaX):
        if deltaX == 0:
            return
        self.x += deltaX

        if self.btNode is None:
            return

        if self.left:
            self.left.translateX(deltaX)

        if self.right:
            self.right.translate(deltaX)

    def balance(self, left, right):
        if left is None or right is None:
            return

        delta_left = self.x - left.rightX()
        delta_right = right.x - self.rightX()
        delta = max(delta_left, delta_right)

        new_rightX = self.rightX() + delta
        right.translateX(new_rightX - right.x)

        new_leftX = self.x - delta - left.width
        left.translateX(new_leftX - left.x)

class LevelInfo(object):
    def __init__(self, left, right):
        self.leftX = left.left_bound()
        self.rightX = right.right_bound()
