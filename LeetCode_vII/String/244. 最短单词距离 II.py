"""
@author: xiongbiao
@date: 2022-02-27 21:42
"""
class WordDistance:

    def __init__(self, wordsDict):
        from collections import defaultdict
        self.word_map = defaultdict(list)

        for i, w in enumerate(wordsDict):
            self.word_map[w].append(i)



    def shortest(self, word1, word2):
        index1 = self.word_map[word1]
        index2 = self.word_map[word2]
        dis = float('inf')
        l1, l2 = 0, 0
        while l1 < len(index1) and l2 < len(index2):
            dis = min(dis, abs(index2[l2] - index1[l1]))
            if index1[l1] < index2[l2]:
                l1 += 1
            else:
                l2 += 1
        return dis


w = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print(w.shortest("coding", "practice"))
print(w.shortest("makes", "coding"))
