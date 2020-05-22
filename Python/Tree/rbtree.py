## written by xiongbiao
## date 2020-5-20

from Tree.bbstree import BalancedBinarySearchTree
from enum import Enum



class RedBlackTree(BalancedBinarySearchTree):

    class Color(Enum):
        RED = 1
        BLACK = 2

    class RBNode(BalancedBinarySearchTree.Node):
        def __init__(self, value, parent):
            super().__init__(value, parent)
            self.color = RedBlackTree.Color.RED


    def __init__(self):
        super().__init__()

    '''
    红黑树添加节点一共有12种情况
    1. 插入的节点没有父节点，染黑，结束
    2. 插入的节点的父节点是黑色，结束 （4种）
    3. 插入的节点的父节点是红色 （8种）
       1）uncle不是红色（说明234树叶子节点没满）（4种）
          LL/RR，祖父节点染成红色，父节点染成黑色，右左旋转祖父节点
          LR/RL，祖父节点染成红色，插入节点染成黑色，左右旋转父节点变成LL/RR，右左旋转父节点
       2）uncle是红色（说明234树叶子节点满了）（4种）
          父节点染成黑色，uncle节点染成黑色，祖父节点染成红色
          祖父节点上溢（当做一个新添加的节点插在234树的上一层）
    '''
    def after_add(self, node):

        parent = node.parent
        if parent is None:
            self.black(node)
            return
        if self.is_black(parent):
            return

        uncle = parent.sibling()
        grand = self.red(parent.parent)
        if self.is_red(uncle):
            self.black(parent)
            self.black(uncle)
            self.after_add(grand)
            return

        if parent.is_left_child():
            if node.is_left_child():
                self.black(parent)
            else:
                self.black(node)
                self.rotate_left(parent)
            self.rotate_right(grand)

        else:
            if node.is_left_child():
                self.black(node)
                self.rotate_right(parent)
            else:
                self.black(parent)
            self.rotate_left(grand)

    '''
    需要再复习一遍
    '''
    def after_remove(self, node):

        if self.is_red(node):
            self.black(node)
            return

        parent = node.parent

        if parent is None:
            return

        left = parent.left is None or node.is_left_child()

        if left:
            sibling = parent.right
        else:
            sibling = parent.left

        if left:
            if self.is_red(sibling):
                self.black(sibling)
                self.red(parent)
                self.rotate_left(parent)
                sibling = parent.right

            if self.is_black(sibling.left) and self.is_black(sibling.right):
                black_parent = self.is_black(parent)
                self.red(sibling)
                self.black(parent)
                if black_parent:
                    self.after_remove(parent)

            else:
                if self.is_black(sibling.right):
                    self.rotate_right(sibling)
                    sibling = parent.right
                self.black(sibling.right)
                self.black(parent)
                self.color(sibling, self.color_of(parent))
                self.rotate_left(parent)
        else:
            if self.is_red(sibling):
                self.black(sibling)
                self.red(parent)
                self.rotate_right(parent)
                sibling = parent.left

            if self.is_black(sibling.left) and self.is_black(sibling.right):
                black_parent = self.is_black(parent)
                self.red(sibling)
                self.black(parent)
                if black_parent:
                    self.after_remove(parent)

            else:
                if self.is_black(sibling.left):
                    self.rotate_left(sibling)
                    sibling = parent.left
                self.black(sibling.left)
                self.black(parent)
                self.color(sibling, self.color_of(parent))
                self.rotate_right(parent)


    def create_node(self, value, parent):
        return RedBlackTree.RBNode(value, parent)

    '''
    颜色函数，判断颜色以及节点染色
    '''
    def color(self, node, color):
        if node is None:
            return node
        node.color = color
        return node

    def black(self, node):
        return self.color(node, RedBlackTree.Color.BLACK)

    def red(self, node):
        return self.color(node, RedBlackTree.Color.RED)

    def color_of(self, node):
        if node:
            return node.color
        return RedBlackTree.Color.BLACK

    def is_black(self, node):
        return self.color_of(node) is RedBlackTree.Color.BLACK

    def is_red(self, node):
        return self.color_of(node) is RedBlackTree.Color.RED

    def show(self, levels):
        for key, value in levels.items():

            for v in value:
                if v.value is None:
                    print('N', end=' ')
                else:
                    print('{}({})'.format(v.value, v.color), end=' ')
            print()

def test_func():
    nodes = [70, 84, 71, 56, 79, 72, 42]
    tree = RedBlackTree()
    for n in nodes:
        tree.add_value(n)

    tree.remove_value(42)
    tree.remove_value(56)
    tree.remove_value(70)
    tree.remove_value(84)
    tree.print()
    print('--------------------')