## written by xiongbiao
## date 2020-6-1
from Tree.node import TreeNode
'''
给定一个有 N 个节点的二叉树，每个节点都有一个不同于其他节点且处于 {1, ..., N} 中的值。
通过交换节点的左子节点和右子节点，可以翻转该二叉树中的节点。
考虑从根节点开始的先序遍历报告的 N 值序列。将这一 N 值序列称为树的行程。
（回想一下，节点的先序遍历意味着我们报告当前节点的值，然后先序遍历左子节点，再先序遍历右子节点。）
我们的目标是翻转最少的树中节点，以便树的行程与给定的行程 voyage 相匹配。 
'''
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.flip = []
        self.index = 1

        def dfs(node):
            if node is None:
                return
            if node.val != voyage[self.index]:
                self.flip.append(-1)
                return

            self.index += 1

            if node.left and voyage[self.index] != node.left.val:
                self.flip.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        if self.flip and self.flip[0] == -1:
            self.flip = [-1]
        return self.flip

