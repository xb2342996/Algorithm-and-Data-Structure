## written by xiongbiao
## date 2020-5-31
from Tree.node import TreeNode

'''
设计一个序列化和反序列化 N 叉树的算法。一个 N 叉树是指每个节点都有不超过 N 个孩子节点的有根树。序列化 / 反序列化算法的算法实现没有限制。
你只需要保证 N 叉树可以被序列化为一个字符串并且该字符串可以被反序列化成原树结构即可。
'''
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: Node
        :rtype: str
        """
        res = []
        def dfs(root):
            res.append(root.val)
            res.append(len(root.children))

            for c in root.children:
                dfs(c)
        dfs(root)
        return ','.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: Node
        """
        data = data.split(',')

        def dfs():
            root = Node(int(data.pop(0)), [])
            num = int(data.pop(0))
            for _ in range(num):
                root.children.append(dfs())
            return root

        return dfs()

print(','.join(['']))


