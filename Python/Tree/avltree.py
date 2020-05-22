## written by xiongbiao
## date 2020-5-20


from Tree.bbstree import BalancedBinarySearchTree




class AVLTree(BalancedBinarySearchTree):
    class AVLNode(BalancedBinarySearchTree.Node):
        def __init__(self, value, parent):
            super().__init__(value, parent)
            self._height = 1

        '''
        AVL树节点方法：更新节点的高度，用于平衡后重新计算节点的高度
        '''

        def update_height(self):
            if self.left:
                left_height = self.left._height
            else:
                left_height = 0

            if self.right:
                right_height = self.right._height
            else:
                right_height = 0

            self._height = 1 + max(left_height, right_height)

        '''
        AVL树节点方法：计算节点的平衡因子，计算当前节点的左右子树的高度差
        '''

        def balance_factor(self):
            if self.left:
                left_height = self.left._height
            else:
                left_height = 0

            if self.right:
                right_height = self.right._height
            else:
                right_height = 0
            return left_height - right_height

        '''
        AVL树节点方法：获取左右子节点高度高的那棵子树，用于AVL树添加删除后旋转中提取不平衡的子树的节点，
                     如果2个子树高度一样，返回同方向节点
        '''

        def taller_child(self):
            if self.left:
                left_height = self.left._height
            else:
                left_height = 0

            if self.right:
                right_height = self.right._height
            else:
                right_height = 0

            if left_height > right_height:
                return self.left
            if left_height < right_height:
                return self.right

            if self.is_left_child():
                return self.left
            else:
                return self.right

    def __init__(self):
        super().__init__()
    '''
    创建AVL节点
    '''
    def create_node(self, value, parent):
        return AVLTree.AVLNode(value, parent)

    '''
    添加节点后，顺着节点的父节点向上找，若节点平衡更新节点高度，找到第一个不平衡的节点，平衡该节点，结束
    '''
    def after_add(self, node):
        node = node.parent
        while node:
            if self.is_balance(node):
                self.update_height(node)
            else:
                self.rebalance(node)
                break
            node = node.parent

    '''
    删除节点后，顺着节点的父节点向上找，若节点平衡更新节点高度，找到不平衡的节点，平衡该节点，直至root
    '''
    def after_remove(self, node):
        node = node.parent
        while node:
            if self.is_balance(node):
                self.update_height(node)
            else:
                self.rebalance(node)
            node = node.parent

    '''
    判断节点是否平衡，节点平衡因子绝对值<=1
    '''
    def is_balance(self, node):
        return abs(node.balance_factor()) <= 1

    '''
    更新节点高度
    '''
    def update_height(self, node):
        node.update_height()

    '''
    平衡节点，找到节点的子节点中高的子节点和孙子节点中高的子节点，判断子节点与孙子节点的方向，旋转相应的节点
    1. LL：parent是grand的left，child是parent的left，右旋grand
    2. LR：parent是grand的left，child是parent的right，左旋parent，变成LL，右旋grand
    3. RL：parent是grand的right，child是parent的left，右旋parent，变成RR，，左旋grand
    4. RR：parent是grand的right，child是parent的right，左旋grand
    '''
    def rebalance(self, grand):
        parent = grand.taller_child()
        child = parent.taller_child()

        if parent.is_left_child():
            if child.is_left_child():
                self.rotate_right(grand)
            else:
                self.rotate_left(parent)
                self.rotate_right(grand)
        else:
            if child.is_left_child():
                self.rotate_right(parent)
                self.rotate_left(grand)
            else:
                self.rotate_left(grand)

    def after_rotate(self, grand, parent, child):
        super().after_rotate(grand, parent, child)
        self.update_height(grand)
        self.update_height(parent)

# nodes = [67, 81, 77, 60, 11, 87, 89, 84, 69]
# tree = AVLTree()
# for n in nodes:
#     tree.add_value(n)
#
# tree.remove_value(11)
# tree.remove_value(60)
# tree.remove_value(67)
# tree.print()