## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。
「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。
'''
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.count = 0
        def dfs(node, maxVal):
            if node is None:
                return

            if node.val >= maxVal:
                self.count += 1
            maxVal = max(maxVal, node)

            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        dfs(root, root.val)
        print(self.count)
        return self.count
