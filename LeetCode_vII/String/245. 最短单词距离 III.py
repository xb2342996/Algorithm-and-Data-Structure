"""
@author: xiongbiao
@date: 2022-02-27 22:32
"""

class Solution:
    def shortestWordDistance(self, wordsDict, word1, word2):
        from collections import defaultdict
        word_map = defaultdict(list)
        for i, w in enumerate(wordsDict):
            word_map[w].append(i)

        indexs_1 = word_map[word1]
        indexs_2 = word_map[word2]
        dis = float('inf')
        if word1 == word2:
            for i in range(len(indexs_1) - 1):
                dis = min(dis, abs(indexs_1[i] - indexs_1[i + 1]))
        else:
            l1, l2 = 0, 0
            while l1 < len(indexs_1) and l2 < len(indexs_2):
                dis = min(dis, abs(indexs_2[l2] - indexs_1[l1]))
                if indexs_1[l1] < indexs_2[l2]:
                    l1 += 1
                else:
                    l2 += 1
        return dis

print(Solution().shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'coding'))
print(Solution().shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'makes'))


