## written by xiongbiao
## date 2020-6-1
from Tree.node import TreeNode
from LinkedList.node import ListNode
'''
给定一个二叉树，编写一个函数来获取这个树的最大宽度。
树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。
每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。
'''
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, head)

    def dfs(self, node, head):
        if head is None:
            return True
        if node is None:
            return False

        if node.val != head.val:
            return

        return self.dfs(node.left, head.next) or self.dfs(node.right, head.next)