## written by xiongbiao
## date 2020-6-1

from Tree.node import TreeNode

'''
给定一个二叉树，找到其中最大的二叉搜索树（BST）子树，其中最大指的是子树节点数最多的。
注意:
子树必须包含其所有后代。
'''
class Solution(object):

    '''
    设计一个节点信息类，类内存储二叉搜索树的跟节点，二叉搜索树的子节点数，二叉搜索树中的最大值和最小值
    后续遍历二叉搜索树，判断每个节点是不是二叉搜索树通过节点信息类存储树这个节点下的最大二叉搜索树。
    如果这个节点的左节点的二叉搜索树的根节点就是这个节点的左节点，左节点的最大值小于这个节点，并且节点的右节点的二叉搜索树的根节点就是这个节点的右节点，右节点的最小值大于这个节点
    这个节点与他的左右节点构成一个最大的二叉搜索树。二叉搜索树的最大值为右节点的最大值
    如果左右子树不空，这个节点与左右子树不能构成一个新的二叉搜索树，这个节点的最大二叉搜索树等于左右子树中size大的那个
    剩下左子树不空或者右子树不空，这个节点的最大二叉搜索树为不空那个树的二叉搜索树
    '''
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.getInfo(root).size

    class Info(object):
        def __init__(self, root, size, min_val, max_val):
            self.root = root
            self.size = size
            self.minVal = min_val
            self.maxVal = max_val

    def getInfo(self, node):
        if node is None:
            return None

        leftInfo = self.getInfo(node.left)
        rightInfo = self.getInfo(node.right)

        left_size, right_size = -1, -1
        left_min, right_max = node.val, node.val
        if leftInfo is None:
            left_size = 0
        elif leftInfo.root == node.left and leftInfo.maxVal < node.val:
            left_size = leftInfo.size
            left_min = leftInfo.minVal

        if rightInfo is None:
            right_size = 0
        elif rightInfo.root == node.right and rightInfo.minVal > node.val:
            right_size = rightInfo.size
            right_max = rightInfo.maxVal

        if left_size >= 0 and right_size >= 0:
            return Solution.Info(node, 1 + left_size + right_size, left_min, right_max)

        if leftInfo and rightInfo:
            if leftInfo.size > rightInfo.size:
                return leftInfo
            else:
                return rightInfo

        return leftInfo if leftInfo else rightInfo


