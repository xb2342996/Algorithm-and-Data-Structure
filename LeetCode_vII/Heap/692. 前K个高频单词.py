# written by xiongbiao
# date 2020-11-22

'''
给一非空的单词列表，返回前 k 个出现次数最多的单词。
'''

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        import heapq

        word_dict = Counter(words)
        sorted_words = sorted(word_dict, key=lambda x: x)
        return heapq.nlargest(k, sorted_words, key=lambda x:word_dict[x])


print(Solution().topKFrequent(["aaa","aa","a"], k = 1))