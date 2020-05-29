## written by xiongbiao
## date 2020-5-27

'''
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词
'''

class Solution(object):

    '''
    使用队列广度优先遍历 + 剪枝，访问每个节点的neighbor，去掉访问过的节点
    '''
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []

        return self.levelSearch(beginWord, endWord, wordList)

    def levelSearch(self, begin, end, wordList):
        queue = []
        visited = set()
        paths, ans = [begin], []
        queue.append(paths)
        visited.add(begin)
        wordList = set(wordList)
        found = False
        while queue:
            subVisited = set()
            size = len(queue)
            for _ in range(size):
                path = queue.pop(0)
                neighbor = self.nextWords(path[-1], wordList)
                for n in neighbor:
                    if n not in visited:
                        if end == n:
                            found = True
                            path.append(n)
                            ans.append(path[:])
                            path.pop()
                        path.append(n)
                        queue.append(path[:])
                        path.pop()
                        subVisited.add(n)
            visited = visited.union(subVisited)
            if found:
                break
        return ans



    def nextWords(self, word, wordList):
        words = []
        for i in range(len(word)):
            for j in range(97, 127):
                new_word = word[:i] + chr(j) + word[i+1:]
                if new_word == word:
                    continue
                if new_word in wordList and new_word not in words:
                    words.append(new_word)
        return words
    '''
    深度遍历剪枝优化，如果上一层访问过这一层的节点，直接返回
    '''
    # def findLadders(self, beginWord, endWord, wordList):
    #     """
    #     :type beginWord: str
    #     :type endWord: str
    #     :type wordList: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     if endWord not in wordList:
    #         return []
    #     paths = [beginWord]
    #     ans = []
    #     neighbors, depth, self.min = self.neighbors(beginWord, endWord, wordList)
    #     self.ladder(beginWord, endWord, neighbors, depth, paths, ans)
    #     return ans
    #
    # def ladder(self, begin, end, neighbors, depth, paths, ans):
    #     if begin == end:
    #         ans.append(paths[:])
    #         return
    #
    #     for cur_word in neighbors[begin]:
    #         if depth[cur_word] == depth[begin] + 1:
    #             paths.append(cur_word)
    #             self.ladder(cur_word, end, neighbors, depth, paths, ans)
    #             paths.pop()
    #
    # def neighbors(self, begin, end, wordList):
    #     neighbors, depths = {}, {}
    #     queue = []
    #     queue.append(begin)
    #     depths[begin] = 0
    #     level = 0
    #     flag = False
    #     while queue:
    #         level += 1
    #         for _ in range(len(queue)):
    #             word = queue.pop(0)
    #             neighbor = self.nextWords(word, wordList)
    #             neighbors[word] = neighbor
    #             for n in neighbor:
    #                 if n not in depths:
    #                     depths[n] = level
    #                     if word == end:
    #                         flag = True
    #                     queue.append(n)
    #         if flag:
    #             break
    #
    #     return neighbors, depths, level
    #
    # def nextWords(self, word, wordList):
    #     words = []
    #     for i in range(len(word)):
    #         for j in range(97, 127):
    #             new_word = word[:i] + chr(j) + word[i+1:]
    #             if new_word == word:
    #                 continue
    #             if new_word in wordList and new_word not in words:
    #                 words.append(new_word)
    #     return words

    '''
    先层序遍历每个节点的下一组节点，找到endword所在的层数，当深度遍历超过这个层数时返回。
    '''
    # def findLadders(self, beginWord, endWord, wordList):
    #     """
    #     :type beginWord: str
    #     :type endWord: str
    #     :type wordList: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     if endWord not in wordList:
    #         return []
    #     paths = [beginWord]
    #     ans = []
    #     neighbors, self.min = self.neighbors(beginWord, endWord, wordList)
    #     print(self.min)
    #     self.ladder(beginWord, endWord, neighbors, paths, ans)
    #     return ans
    #
    # def ladder(self, begin, end, neighbors, paths, ans):
    #     if begin == end:
    #         ans.append(paths[:])
    #         return
    #
    #     if len(paths) == self.min:
    #         return
    #
    #     for cur_word in neighbors[begin]:
    #         if cur_word in paths:
    #             continue
    #         paths.append(cur_word)
    #         self.ladder(cur_word, end, neighbors, paths, ans)
    #         paths.pop()
    #
    # def neighbors(self, begin, end, wordList):
    #     neighbors = {}
    #     queue = []
    #     queue.append(begin)
    #     level = 0
    #     flag = False
    #     while queue:
    #         level += 1
    #         for _ in range(len(queue)):
    #             word = queue.pop(0)
    #             neighbor = self.nextWords(word, wordList)
    #             neighbors[word] = neighbor
    #             for n in neighbor:
    #                 if word == end:
    #                     flag = True
    #                 queue.append(n)
    #         if flag:
    #             break
    #
    #     return neighbors, level
    #
    # def nextWords(self, word, wordList):
    #     words = []
    #     for i in range(len(word)):
    #         for j in range(97, 127):
    #             new_word = word[:i] + chr(j) + word[i+1:]
    #             if new_word == word:
    #                 continue
    #             if new_word in wordList and new_word not in words:
    #                 words.append(new_word)
    #     return words

    '''
    深度优先遍历，获取当前节点的下一个节点数组递归遍历数组内所有元素找到每个元素的下一个节点数组超出长度返回
    '''
    # def findLadders(self, beginWord, endWord, wordList):
    #     """
    #     :type beginWord: str
    #     :type endWord: str
    #     :type wordList: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     if endWord not in wordList:
    #         return []
    #     self.min = float('inf')
    #     paths = [beginWord]
    #     ans = []
    #     self.ladder(beginWord, endWord, wordList, paths, ans)
    #     return ans
    #
    # def ladder(self, begin, end, wordList, paths, ans):
    #     if begin == end:
    #         if self.min > len(paths):
    #             ans.clear()
    #             ans.append(paths[:])
    #             self.min = len(paths)
    #         elif self.min == len(paths):
    #             ans.append(paths[:])
    #         return
    #
    #     if len(paths) > self.min:
    #         return
    #
    #     for word in self.nextWord(begin, wordList):
    #         if word in paths:
    #             continue
    #         paths.append(word)
    #         self.ladder(word, endWord, wordList, paths, ans)
    #         paths.pop()
    #     return
    #
    # def nextWord(self, curWord, wordList):
    #     res = []
    #     for i in range(len(curWord)):
    #         for j in range(97, 126):
    #             word = curWord[:i] + chr(j) + curWord[i+1:]
    #             if word in wordList and word not in res:
    #                 res.append(word)
    #
    #     return res

    '''
    深度优先遍历，依次递归判断列表中没一个元素是否是由前一个元素转换的
    '''
    # def findLadders(self, beginWord, endWord, wordList):
    #     """
    #     :type beginWord: str
    #     :type endWord: str
    #     :type wordList: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     if endWord not in wordList:
    #         return []
    #     self.min = float('inf')
    #     ans = []
    #     paths = [beginWord]
    #     self.ladder(beginWord, endWord, wordList, paths, ans)
    #     return ans
    #
    #
    # def ladder(self, begin, end, wordList, paths, ans):
    #     if begin == end:
    #         if self.min > len(paths):
    #             ans.clear()
    #             self.min = len(paths)
    #             ans.append(paths[:])
    #         elif self.min == len(paths):
    #             ans.append(paths[:])
    #
    #     if len(paths) >= self.min:
    #         return
    #
    #     for i in range(len(wordList)):
    #         cur_word = wordList[i]
    #
    #         if cur_word in paths:
    #             continue
    #
    #         if self.oneChange(begin, cur_word):
    #             paths.append(cur_word)
    #             self.ladder(cur_word, endWord, wordList, paths, ans)
    #             paths.pop()
    #
    #
    # def oneChange(self, word_1, word_2):
    #     count = 0
    #     for i in range(len(word_1)):
    #         if word_1[i] != word_2[i]:
    #             count += 1
    #         if count >= 2:
    #             return False
    #     return count == 1


    # def findLadders(self, beginWord, endWord, wordList):
    #     """
    #     :type beginWord: str
    #     :type endWord: str
    #     :type wordList: List[str]
    #     :rtype: List[List[str]]
    #     """
    #     wordList = set(wordList)
    #     if endWord not in wordList:
    #         return []
    #
    #     result = []
    #     forward, backward = {beginWord: [[beginWord]]}, {endWord: [[endWord]]}
    #     length = 2
    #     visited = set()
    #     while forward:
    #         if len(forward) > len(backward):
    #             forward, backward = backward, forward
    #         tmp = {}
    #         while forward:
    #             word, paths = forward.popitem()
    #             visited.add(word)
    #             for i in range(len(word)):
    #                 for s in range(97, 126):
    #                     new = word[:i] + chr(s) + word[i + 1:]
    #                     if new in backward:
    #                         if paths[0][0] == beginWord:
    #                             for f_path in paths:
    #                                 for b_path in backward[new]:
    #                                     result.append(f_path + b_path[::-1])
    #                         else:
    #                             for f_path in paths:
    #                                 for b_path in backward[new]:
    #                                     result.append(b_path + f_path[::-1])
    #                     if new in wordList and new not in visited:
    #                         tmp[new] = tmp.get(new, []) + [path + [new] for path in paths]
    #         length += 1
    #         if result and length > len(result[0]):
    #             break
    #         forward = tmp
    #     return result


beginWord = 'hit'
endWord = 'cog'
wordList = ["hot","dot","dog","lot","log","cog"]

print(Solution().findLadders(beginWord, endWord, wordList))
