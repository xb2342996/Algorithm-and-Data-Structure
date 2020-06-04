## written by xiongbiao
## date 2020-6-4
from Tree.node import TreeNode
'''
返回与给定的前序和后序遍历匹配的任何二叉树。
'''
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        count = 1
        ans, level = [], []
        while queue:
            node = queue.pop(0)
            level.append(node.val)
            count -= 1
            for child in node.children:
                queue.append(child)

            if count == 0:
                ans.append(level)
                count = len(queue)

        return ans