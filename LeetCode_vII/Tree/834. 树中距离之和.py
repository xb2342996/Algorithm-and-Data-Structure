## written by xiongbiao
## date 2020-5-31

'''
给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1 条边 。
第 i 条边连接节点 edges[i][0] 和 edges[i][1] 。
返回一个表示节点 i 与其他所有节点距离之和的列表 ans。
'''
class Solution(object):

    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        ans = [0] * N
        count = [1] * N
        def dfs(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfsAll(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfsAll(child, node)

        dfs()
        dfsAll()
        return ans

    '''
    深度优先遍历，超时
    '''
    # def sumOfDistancesInTree(self, N, edges):
    #     """
    #     :type N: int
    #     :type edges: List[List[int]]
    #     :rtype: List[int]
    #     """
    #     from collections import defaultdict
    #     edge_dict = defaultdict(list)
    #     for e1, e2 in edges:
    #         edge_dict[e1].append(e2)
    #         edge_dict[e2].append(e1)
    #
    #     res = []
    #     for i in range(N):
    #         self.ans = 0
    #         total = 0
    #         for j in range(N):
    #             if i != j:
    #                 self.visited = set()
    #                 self.visited.add(i)
    #                 self.dfs(i, j, edge_dict, 0,)
    #                 total += self.ans
    #         res.append(total)
    #     return res
    # def dfs(self, start, end, edges, path):
    #     if end in edges[start]:
    #         path += 1
    #         self.ans = path
    #         return
    #     for n in edges[start]:
    #         if n not in self.visited:
    #             self.visited.add(n)
    #             self.dfs(n, end, edges, path+1)




print(Solution().sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))