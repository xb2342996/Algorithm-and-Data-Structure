## written by xiongbiao
## date 2020-6-2

from Tree.node import TreeNode
'''
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。
返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回
'''

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        from collections import defaultdict
        graph = defaultdict(list)

        def dfs(node, parent=None):
            if node is None:
                return
            graph[node].append(parent)
            graph[parent].append(node)
            dfs(node.left, node)
            dfs(node.right, node)

        self.ans = []
        dfs(root)
        queue = [node for node in graph if node == target]
        distance = K
        count = 1
        visited = set(queue)
        while queue and distance >= 0:
            node = queue.pop(0)
            count -= 1
            if node and distance == 0:
                self.ans.append(node.val)
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
            if count == 0:
                count = len(queue)
                distance -= 1
        return self.ans