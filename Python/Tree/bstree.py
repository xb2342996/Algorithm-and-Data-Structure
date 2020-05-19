## written by xiongbiao
## date 2020-5-19

from Tree.tree import BinaryTree, Node

class BinarySearchTree(BinaryTree):

    def __init__(self):
        super().__init__()


    def add_node(self, value):
        self._check_value(value)

        new_node = Node(value, None)
        if self._root is None:
            self._root = new_node
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

        self._size += 1

    def _check_value(self, value):
        if value is None:
            raise ValueError('node value cannot be None')

nodes = [7, 4, 9, 2, 5, 8, 11, 3]
tree = BinarySearchTree()
for n in nodes:
    tree.add_node(n)

print(tree.inorder_traversal('recursive'))
print(tree.preorder_traversal('recursive'))
print(tree.postorder_traversal('recursive'))
tree.reverse()
tree.print()