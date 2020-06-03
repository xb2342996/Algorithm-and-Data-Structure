## written by xiongbiao
## date 2020-6-3

from Tree.node import TreeNode
'''
给出二叉树的根节点 root，树上每个节点都有一个不同的值。
如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
'''
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        self.forest = []
        self.node_list = []
        self.search(root, None, to_delete)
        if root.val not in to_delete:
            self.forest.append(root)
        return self.forest


    def search(self, node, parent, to_delete):
        if node is None:
            return

        self.search(node.left, node, to_delete)
        self.search(node.right, node, to_delete)

        if node.val in to_delete:
            if parent:
                if parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None
            if node.left:
                self.forest.append(node.left)
            if node.right:
                self.forest.append(node.right)




