## written by xiongbiao
## date 2020-6-2
from Tree.node import TreeNode

'''
给定一个 每个结点的值互不相同 的二叉树，和一个目标值 k，找出树中与目标值 k 最近的叶结点。 
这里，与叶结点 最近 表示在二叉树中到达该叶节点需要行进的边数与到达其它叶结点相比最少。
而且，当一个结点没有孩子结点时称其为叶结点。
'''
class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
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

        dfs(root)
        queue = [node for node in graph if node and node.val == k]
        visited = set(queue)

        while queue:
            node = queue.pop(0)
            if node:
                if len(graph[node]) <= 1:
                    return node.val

                for n in graph[node]:
                    if n not in visited:
                        visited.add(n)
                        queue.append(n)