## written by xiongbiao
## date 2020-5-20

from Tree.bstree import BinarySearchTree

class BalancedBinarySearchTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    '''
        右旋：找到grand的左节点parent和parent的右节点child，更改parent，child，更新grand的父节点的左右子节点
              更新grand和parent节点的高度
                  g                      p 
                /   \                  /   \
               p    t3      --->      n     g
             /  \                    / \   / \
            n    t2                 t0 t1 t2 t3
           / \
          t0  t1
          g为不平衡的节点，g左子树高度 - g右子树高度 > 1
        '''

    def rotate_right(self, grand):
        parent = grand.left
        child = parent.right

        grand.left = child
        parent.right = grand

        self.after_rotate(grand, parent, child)

    '''
    左旋：与右旋对称
    '''

    def rotate_left(self, grand):
        parent = grand.right
        child = parent.left

        grand.right = child
        parent.left = grand

        self.after_rotate(grand, parent, child)

    def after_rotate(self, grand, parent, child):
        parent.parent = grand.parent
        if grand.is_left_child():
            grand.parent.left = parent
        elif grand.is_right_child():
            grand.parent.right = parent
        else:
            self._root = parent

        if child:
            child.parent = grand
        grand.parent = parent

