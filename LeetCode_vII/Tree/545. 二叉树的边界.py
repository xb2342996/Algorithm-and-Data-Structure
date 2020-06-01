## written by xiongbiao
## date 2020-6-1

from Tree.node import TreeNode

'''
给定一棵二叉树，以逆时针顺序从根开始返回其边界。边界按顺序包括左边界、叶子结点和右边界而不包括重复的结点。 (结点的值可能重复)
左边界的定义是从根到最左侧结点的路径。右边界的定义是从根到最右侧结点的路径。若根没有左子树或右子树，则根自身就是左边界或右边界。注意该定义只对输入的二叉树有效，而对子树无效。
最左侧结点的定义是：在左子树存在时总是优先访问，如果不存在左子树则访问右子树。重复以上操作，首先抵达的结点就是最左侧结点。
最右侧结点的定义方式相同，只是将左替换成右。
'''

class Solution(object):
    '''

    '''
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.left = []
        self.right = []
        self.leaves = []
        self.preorder(root, 0)
        print(self.left)
        print(self.right)
        print(self.leaves)
        self.left.extend(self.leaves)
        self.left.extend(self.right[::-1])
        return self.left

    def isRoot(self, flag):
        return flag == 0

    def isLeftBound(self, flag):
        return flag == 1

    def isRightBound(self, flag):
        return flag == 2

    def isLeaf(self, node):
        return node.left is None and node.right is None

    def leftChildFlag(self, node, flag):
        if self.isLeftBound(flag) or self.isRoot(flag):
            return 1
        elif self.isRightBound(flag) and node.right is None:
            return 2
        else:
            return 3

    def rightChildFlag(self, node, flag):
        if self.isRightBound(flag) or self.isRoot(flag):
            return 2
        elif self.isLeftBound(flag) and node.left is None:
            return 1
        else:
            return 3

    def preorder(self, node, flag):
        if node is None:
            return
        if self.isRoot(flag) or self.isLeftBound(flag):
            self.left.append(node.val)
        elif self.isRightBound(flag):
            self.right.append(node.val)
        elif self.isLeaf(node):
            self.leaves.append(node.val)

        self.preorder(node.left, self.leftChildFlag(node, flag))
        self.preorder(node.right, self.rightChildFlag(node, flag))
