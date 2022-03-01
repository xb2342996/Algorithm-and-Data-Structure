"""
@author: xiongbiao
@date: 2022-03-01 22:25
"""

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from collections import defaultdict
        map = defaultdict(int)
        for w in s:
            map[w] += 1

        single, character = 0, None
        for k, v in map.items():
            if v % 2 != 0:
                single += 1
                character = k
        if single > 1:
            return []

        length = len(s)
        mid = length // 2
        string = ''
        if single == 1:
            map[mid] -= 1

        words = []
        for k, v in map.items():
            for i in range(v // 2):
                words.append(k)

        ans = set()
        used = [False] * len(words)
        def dfs(words, used, sub):
            if len(sub) == len(words):
                ans.add(sub)
                return

            for i, w in enumerate(words):
                if not used[i]:
                    used[i] = True
                    dfs(words, used, sub + w)
                    used[i] = False

        dfs(words, used, '')
        res = []
        for w in ans:
            m = ''
            if character:
                m = character
            res.append(w + m + w[::-1])
        return res



Solution().generatePalindromes("abb")
