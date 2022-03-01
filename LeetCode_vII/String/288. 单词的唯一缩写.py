"""
@author: xiongbiao
@date: 2022-03-01 23:52
"""

class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        from collections import defaultdict
        self.map = defaultdict(set)
        for d in dictionary:
            w = self.calc_abbr(d)
            self.map[w].add(d)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        w = self.calc_abbr(word)
        if w not in self.map:
            return True

        if w in self.map.keys() and word in self.map[w] and len(self.map[w]) == 1:
            return True

        return False

    def calc_abbr(self, word):
        if len(word) < 3:
            return word
        size = len(word) - 2
        w = word[0] + str(size) + word[-1]
        return w

v = ValidWordAbbr(["a", "a"])
print(v.isUnique("a"))
# print(v.isUnique("cart"))
# print(v.isUnique("cane"))
# print(v.isUnique("make"))
# print(v.isUnique("cake"))