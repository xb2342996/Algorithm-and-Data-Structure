## written by xiongbiao
## date 2020-5-19

from Tree.tree import BinaryTree, Node

class BinarySearchTree(BinaryTree):

    def __init__(self):
        super().__init__()


    def add_value(self, value):

        self._check_value(value)
        new_node = self.create_node(value, None)
        if self._root is None:
            self._root = new_node
            self.after_add(new_node)
            return

        node = self._root
        parent = self._root
        while node:
            parent = node
            if node.value > value:
                node = node.left
            elif node.value < value:
                node = node.right
            else:
                node.value = value
                return
        if parent.value > value:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.parent = parent

        self.after_add(new_node)
        self._size += 1

    def after_add(self, node):
        pass


    def remove_value(self, value):
        self._remove_node(self._get_node(value))

    def _remove_node(self, node):
        if node is None:
            return None

        if node.has_two_children():
            replace = self.successor(node)
            node.value = replace.value
            node = replace

        if node.left:
            child = node.left
        else:
            child = node.right

        if child:
            child.parent = node.parent
            if node.parent.left == node:
                node.parent.left = child
            elif node.parent.right == node:
                node.parent.right = child
            else:
                self._root = child
            self.after_remove(child)
        elif node.parent is None:
            self._root = None
            self.after_remove(node)
        else:
            if node.is_left_child():
                node.parent.left = None
            elif node.is_right_child():
                node.parent.right = None
            self.after_remove(node)

        self._size -= 1

    def after_remove(self, node):
        pass

    def create_node(self, value, parent):
        return Node(value, parent)

    def _get_node(self, value):

        node = self._root
        while node:
            if node.value > value:
                node = node.left
            elif node.value < value:
                node = node.right
            else:
                return node
        return None

    def _check_value(self, value):
        if value is None:
            raise ValueError('node value cannot be None')

# nodes = [7, 4, 9, 2, 5, 8, 11, 3]
# tree = BinarySearchTree()
# for n in nodes:
#     tree.add_value(n)
#
# # print(tree.inorder_traversal('recursive'))
# # print(tree.preorder_traversal('recursive'))
# # print(tree.postorder_traversal('recursive'))
# # tree.reverse()
# tree.remove_value(7)
# tree.remove_value(9)
# tree.print()