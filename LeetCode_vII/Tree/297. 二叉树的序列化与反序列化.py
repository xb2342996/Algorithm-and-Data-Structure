## written by xiongbiao
## date 2020-5-31
from Tree.node import TreeNode

'''
请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
'''

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None

        queue = []
        queue.append(root)
        strs = []
        while queue:
            node = queue.pop(0)
            if node:
                strs.append(str(node.val))
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
            else:
                strs.append('None')

        while strs[-1] is 'None':
            strs.pop()

        return ','.join(strs)


    def deserialize(self, data):
            """Decodes your encoded data to tree.

            :type data: str
            :rtype: TreeNode
            """
            if len(data) == 0:
                return None

            data = data.split(',')
            queue = []
            root = TreeNode(data.pop(0))
            queue.append(root)

            while len(data) > 0:
                node = queue.pop(0)
                left = data.pop(0)
                if left != 'None':
                    node.left = TreeNode(int(left))
                    queue.append(node.left)
                if len(data) > 0:
                    right = data.pop(0)
                    if right != 'None':
                        node.right = TreeNode(int(right))
                        queue.append(node.right)

            return root
